#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import argparse

from jiebarpc import JiebaRPCServer, JiebaRPCDispatcher


def main(host, port, processnum=1):
    server = JiebaRPCServer(JiebaRPCDispatcher(processnum))
    server.listen(host, port)
    server.start()
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'python -m jiebarpc',
        description='Run jiebarpc server'
    )
    parser.add_argument('-n', '--processnum', type=int, default=1,
                        help='How many processes to use.')
    parser.add_argument('address',
                        help='Server listen address like localhost:8888',)
    ns = parser.parse_args()

    address = ns.address.split(':')
    host = address[0]
    port = int(address[1])

    sys.exit(main(host, port, ns.processnum))
