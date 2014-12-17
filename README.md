jieba-rpc
=============
[![Build Status](https://travis-ci.org/messense/jieba-rpc.svg?branch=master)](https://travis-ci.org/messense/jieba-rpc)

Simple [jieba](https://github.com/fxsjy/jieba) RPC server based on [msgpack-rpc-python](https://github.com/msgpack-rpc/msgpack-rpc-python).


## Installation

Install `jieba-rpc` using `pip`:

```bash
pip install jieba-rpc
```


## Usage

You can start a simple jieba RPC server by executing:

```bash
python -m jiebarpc localhost:8888
```

Or if you wish to customize it using codes:

```python
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
    sys.exit(main(host, port)) -*- coding: utf-8 -*-
```


## License

The MIT License (MIT)

Copyright (c) 2014 messense

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
