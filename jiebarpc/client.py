# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import msgpackrpc


class JiebaRPCClient(msgpackrpc.Client):

    def __init__(self, host, port, *args, **kwargs):
        address = msgpackrpc.Address(host, port)
        super(JiebaRPCClient, self).__init__(address, *args, **kwargs)


if __name__ == '__main__':
    client = JiebaRPCClient('localhost', 4444)
    print(client.call('cut', '测试分词'))
    print(client.call('cut_for_search', '测试分词'))
    print(client.call('extract_tags', '测试分词'))
    print(client.call('textrank', '测试分词'))
    print(client.call('tokenize', '测试分词'))
    print(client.call('posseg', '测试分词'))
