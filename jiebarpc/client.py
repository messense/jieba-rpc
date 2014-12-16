# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import msgpackrpc


class JiebaRPCClient(msgpackrpc.Client):

    def __init__(self, host, port, *args, **kwargs):
        address = msgpackrpc.Address(host, port)
        super(JiebaRPCClient, self).__init__(address, *args, **kwargs)

    def cut(self, sentence, cut_all=False, HMM=True):
        return self.call(
            'cut',
            sentence,
            cut_all,
            HMM
        )

    def cut_for_search(self, sentence):
        return self.call(
            'cut_for_search',
            sentence
        )

    def extract_tags(self, sentence, topK=20, withWeight=False):
        return self.call(
            'extract_tags',
            sentence,
            topK,
            withWeight
        )

    def textrank(self, sentence, topK=10, withWeight=False):
        return self.call(
            'textrank',
            sentence,
            topK,
            withWeight
        )

    def posseg(self, sentence, HMM=True):
        return self.call(
            'posseg',
            sentence,
            HMM
        )

    def tokenize(self, sentence, mode='default', HMM=True):
        return self.call(
            'tokenize',
            sentence,
            mode,
            HMM
        )

if __name__ == '__main__':
    client = JiebaRPCClient('localhost', 4444)
    print(client.cut('测试分词'))
    print(client.cut_for_search('测试分词'))
    print(client.extract_tags('测试分词'))
    print(client.textrank('测试分词'))
    print(client.tokenize('测试分词'))
    print(client.posseg('测试分词'))
