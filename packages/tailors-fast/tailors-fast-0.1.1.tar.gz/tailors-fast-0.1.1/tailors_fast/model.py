# -*- coding: utf-8 -*-
import os

import fasttext
import hao
from hao.stopwatch import Stopwatch

from . import TailorsError, texts
from .tokenizer import JiebaTokenizer

LOGGER = hao.logs.get_logger(__name__)


class FastModel:

    def __init__(self,
                 path_or_key: str,
                 stopwords_path='data/dict/stopwords.txt',
                 keywords_path='data/dict/keywords.txt') -> None:
        super().__init__()
        self.path_or_key = path_or_key
        self.tokenizer = JiebaTokenizer(stopwords_path=stopwords_path, keywords_path=keywords_path)
        self.model = self.load_model()

    def load_model(self):
        if ".local" in self.path_or_key:
            from hao.oss import init as oss_init
            oss_init(self.path_or_key[: self.path_or_key.rfind(".")])
            model_path = hao.config.get_path(self.path_or_key)
        else:
            model_path = hao.paths.get_path(self.path_or_key)

        if not os.path.exists(model_path):
            raise TailorsError(f"model path not exist: {model_path}")
        LOGGER.info(f"[FastModel] loading from: {model_path}")
        sw = Stopwatch()
        fasttext.FastText.eprint = lambda x: None
        model = fasttext.load_model(model_path)
        LOGGER.info(f"[FastModel] loaded, took: {sw.took()}")
        return model

    def predict(self, text: str, k=1, threshold=0.0):
        text = hao.strings.strip_to_none(text)
        if text is None:
            return None, None
        text = texts.fix_text(text)
        tokenized = self.tokenizer.cut_and_join(text)
        predictions, scores = self.model.predict(tokenized, k=k, threshold=threshold)
        preds = [(p[9:], s) for p, s in zip(predictions, scores)]
        return preds[0] if k == 1 else preds
