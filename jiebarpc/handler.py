# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
import multiprocessing

import jieba
import jieba.analyse
import jieba.posseg

from jiebarpc.utils import to_text


logger = logging.getLogger(__name__)


class JiebaRPCHandler(object):

    def __init__(self, enable_parallel=True):
        logger.info('Initializing jieba...')
        jieba.initialize()
        logger.info('Successfully initialized jieba.')
        if enable_parallel:
            logger.info('Jiea running in parallel mode.')
            jieba.enable_parallel(multiprocessing.cpu_count())

    def cut(self, sentence, cut_all=False, HMM=True):
        segs = jieba.cut(sentence, cut_all=cut_all, HMM=HMM)
        return list(segs)

    def cut_for_search(self, sentence):
        segs = jieba.cut_for_search(sentence)
        return list(segs)

    def extract_tags(self, sentence, topK=20, withWeight=False):
        tags = jieba.analyse.extract_tags(
            sentence,
            topK=topK,
            withWeight=withWeight
        )
        return list(tags)

    def textrank(self, sentence, topK=10, withWeight=False):
        ranks = jieba.analyse.textrank(
            sentence,
            topK=topK,
            withWeight=withWeight
        )
        return list(ranks)

    def posseg(self, sentence, HMM=True):
        words = jieba.posseg.cut(sentence, HMM=HMM)
        segs = [(w.word, w.flag) for w in words]
        return segs

    def tokenize(self, sentence, mode='default', HMM=True):
        sentence = to_text(sentence)
        tokens = jieba.tokenize(sentence, mode=mode, HMM=HMM)
        return list(tokens)
