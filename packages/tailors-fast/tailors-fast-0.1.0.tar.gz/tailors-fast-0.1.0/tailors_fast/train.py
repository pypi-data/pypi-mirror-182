# -*- coding: utf-8 -*-
import datetime
import itertools
import os
from typing import List

import fasttext
import hao
import numpy as np
from hao.namespaces import attr, from_args
from hao.stopwatch import Stopwatch
from sklearn.metrics import classification_report

LOGGER = hao.logs.get_logger(__name__)


PARAM_MAPPING = {
    'train_file': 'input',
    'val_file': 'autotuneValidationFile',
    'tune_time': 'autotuneDuration',
    'tune_size': 'autotuneModelSize',
    'pretrained_file': 'pretrainedVectors',
    'min_count': 'minCount',
    'ngram': 'wordNgrams',
}
FILE_SKIP_ATTR = ('pretrained_file', 'train_file', 'val_file', 'tune_time', 'tune_size')

@from_args
class TrainConf(object):
    exp: str = attr(str, required=True, help='experiment name')
    file_train: str = attr(str, default='data/corpus/fast/train.txt', required=True)
    file_val: str = attr(str, default='data/corpus/fast/val.txt', required=True)
    tune_time: int = attr(int, default=600, help='auto tune duration in seconds')
    tune_size: str = attr(str, default="100M", help='auto tune model size')
    lr: list = attr(List[float], default=[])
    dim: list = attr(List[int], default=[50])
    ws: list = attr(List[int], default=[], help="window size")
    epoch: list = attr(List[int], default=[])
    neg: list = attr(List[int], default=[])
    min_count: list = attr(List[int], default=[30])
    ngram: list = attr(List[int], default=[3])
    minn: list = attr(List[int], default=[])
    maxn: list = attr(List[int], default=[])
    loss: list = attr(List[str], choices=('ns', 'hs', 'softmax', 'ova'), default=[])
    k: int = attr(int, default=1, help='top k')
    threshold: float = attr(float, default=0.0, help='threshold for top k')
    pretrained: str = attr(str)


def train():
    conf = TrainConf()
    LOGGER.info(conf)
    train_file = hao.paths.get(conf.file_train)
    val_file = hao.paths.get(conf.file_val)
    pretrained_file = hao.paths.get(conf.pretrained)
    k = conf.k
    threshold = conf.threshold

    labels_all = get_all_labels([train_file, val_file])

    for lr, dim, epoch, ws, neg, min_count, ngram, minn, maxn, loss in itertools.product(
            conf.lr or [None],
            conf.dim or [None],
            conf.epoch or [None],
            conf.ws or [None],
            conf.neg or [None],
            conf.min_count or [None],
            conf.ngram or [None],
            conf.minn or [None],
            conf.maxn or [None],
            conf.loss or [None]
    ):
        params = {
            'pretrained_file': pretrained_file,
            'train_file': train_file,
            'val_file': val_file,
            'tune_time': conf.tune_time,
            'tune_size': conf.tune_size,
            'lr': lr,
            'dim': dim,
            'epoch': epoch,
            'ws': ws,
            'neg': neg,
            'min_count': min_count,
            'ngram': ngram,
            'minn': minn,
            'maxn': maxn,
            'loss': loss,
        }
        train_and_val(conf.exp, k, threshold, labels_all, **params)


def get_all_labels(files: list):
    labels = set()
    for file in files:
        with open(file) as f:
            for line in f:
                splits = line.split('__label__')
                for s in splits[1:]:
                    labels.add(s.strip())
    return list(labels)


def train_and_val(exp: str, k, threshold, labels_all, **kwargs):
    params = {PARAM_MAPPING.get(k, k): v for k, v in kwargs.items() if v}
    LOGGER.info(f'train: \n{hao.jsons.prettify(params)}')

    sw = Stopwatch()
    date = datetime.datetime.now().strftime('%y%m%d-%H%M')
    model = fasttext.train_supervised(**params)
    LOGGER.info(f"vocab size: {len(model.words)}")
    LOGGER.info(f"labels: {[label[9:] for label in model.labels]}")

    file_val = kwargs.get('val_file')
    n, precision, recall = model.test(file_val, k=k, threshold=threshold)
    f1 = 2 * precision * recall / (precision + recall)
    LOGGER.info(f"val size: {n}, precision: {precision:.4}, recall: {recall:.4}, f1: {f1:.4}")

    model_params = '-'.join([
        f'{k}={v}' for k, v in kwargs.items()
        if k not in FILE_SKIP_ATTR and v is not None
    ])
    model_name = f'{exp}-{date}-{model_params}-f1={f1:.4}.bin'
    model_path = hao.paths.get('data/model', model_name)
    hao.paths.make_parent_dirs(model_path)
    model.save_model(model_path)

    size = round(os.path.getsize(model_path) / (1024*1024), 2)
    LOGGER.info(f'model saved to: {model_path}, size: {size}')
    for att in ('lr', 'dim', 'epoch', 'ws', 'neg', 'minCount', 'wordNgrams', 'minn', 'maxn'):
        LOGGER.info(f'{att: >25}: {getattr(model, att)}')

    lines = open(file_val).readlines()
    splits = [line.split('__label__') for line in lines]
    text, labels = list(zip(*[(s[0].strip(), [l.strip() for l in s[1:]]) for s in splits]))
    preds = [[p[9:] for p in prediction] for prediction in model.predict(list(text), k=k, threshold=threshold)[0]]
    indices_true = to_indices(labels, labels_all)
    indices_pred = to_indices(preds, labels_all)
    report = classification_report(indices_true, indices_pred, target_names=labels_all, digits=4, zero_division=0)
    LOGGER.info(f"\n{' classification report '.center(60, '=')}\n{report}")

    LOGGER.info(f'took: {sw.took()}')
    return model_name, f1


def to_indices(entries: List[list], labels):
    indices_labels = []
    for items in entries:
        indices = [0 for _ in labels]
        for label in items:
            indices[labels.index(label)] = 1
        indices_labels.append(indices)
    return np.array(indices_labels)


if __name__ == '__main__':
    try:
        train()
    except KeyboardInterrupt:
        print('[ctrl-c] stopped')
    except Exception as err:
        LOGGER.exception(err)
