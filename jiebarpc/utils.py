# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from functools import wraps
import six


def to_text(value, encoding='utf-8'):
    """Convert value to unicode, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def ensure_unicode(func):

    def _ensure_unicode(l):
        if isinstance(l, (tuple, list)):
            return [_ensure_unicode(i) for i in l]
        elif isinstance(l, six.string_types):
            return to_text(l)
        else:
            return l

    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return _ensure_unicode(ret)

    return wrapper
