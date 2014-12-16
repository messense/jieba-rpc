#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from jiebarpc import JiebaRPCServer, JiebaRPCDispatcher


def main(host, port):
    server = JiebaRPCServer(JiebaRPCDispatcher())
    server.listen(host, port)
    server.start()
    return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print('Usage: %s host port' % sys.argv[0])
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    sys.exit(main(host, port))
