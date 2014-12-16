# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import msgpackrpc

from jiebarpc.handler import JiebaRPCHandler


class JiebaRPCServer(msgpackrpc.Server):

    def __init__(self, dispatcher=None, *args, **kwargs):
        dispatcher or dispatcher or JiebaRPCHandler()
        super(JiebaRPCServer, self).__init__(
            dispatcher,
            *args,
            **kwargs
        )

    def listen(self, host, port):
        address = msgpackrpc.Address(host, port)
        super(JiebaRPCServer, self).listen(address)


if __name__ == '__main__':
    server = JiebaRPCServer()
    server.listen('localhost', 4444)
    server.start()
