#!/usr/bin/env python
from __future__ import with_statement
import os
import sys
from setuptools import setup, find_packages

readme = 'README.md'
if os.path.exists('README.rst'):
    readme = 'README.rst'
with open(readme) as f:
    long_description = f.read()

requirements = [
    'msgpack-rpc-python',
    'six',
]

if sys.version_info[0] < 3:
    requirements.append('jieba')
else:
    requirements.append('jieba3k')

setup(
    name='jieba-rpc',
    version='0.0.4',
    author='messense',
    author_email='messense@icloud.com',
    url='https://github.com/messense/jieba-rpc',
    packages=find_packages(),
    keywords='jieba, rpc',
    description='jieba RPC server',
    long_description=long_description,
    install_requires=requirements,
    include_package_data=True,
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
