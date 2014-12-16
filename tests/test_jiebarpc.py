# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
import time
import unittest
from subprocess import Popen, PIPE

from jiebarpc import JiebaRPCClient


class JiebaRPCTestCase(unittest.TestCase):

    HOST = 'localhost'
    PORT = '9999'
    SENTENCE = '小明硕士毕业于中国科学院计算所，后在日本京都大学深'

    def setUp(self):
        curr_dir = os.path.abspath(os.path.dirname(__file__))
        server_file = os.path.join(curr_dir, 'server.py')
        self.server = Popen(
            ['python', server_file, self.HOST, self.PORT],
            shell=False,
            stdin=PIPE,
            stderr=PIPE,
            close_fds=True,
        )
        time.sleep(10)
        self.client = JiebaRPCClient(self.HOST, int(self.PORT))

    def tearDown(self):
        try:
            self.server.kill()
        except OSError:
            pass

    def test_cut(self):
        segs = self.client.cut(self.SENTENCE)
        self.assertTrue('小明' in segs)
        self.assertTrue('硕士' in segs)
        self.assertTrue('毕业' in segs)
