# -*- coding: utf-8 -*-

from os import environ
from urllib.parse import urlparse as _urlparse


def lower_dict(d):
    """Lower cases string keys in given dict."""

    _d = {}

    for k, v in d.items():
        try:
            _d[k.lower()] = v
        except AttributeError:
            _d[k] = v

    return _d


def urlparse(d, keys=None):
    """Returns a copy of the given dictionary with url values parsed."""

    d = d.copy()

    if keys is None:
        keys = d.keys()

    for key in keys:
        d[key] = _urlparse(d[key])

    return d


def prefix(prefix):
    """Returns a dictionary of all environment variables starting with
    the given prefix, lower cased and stripped.
    """

    d = {}
    e = lower_dict(environ.copy())

    prefix = prefix.lower()

    for k, v in e.items():
        try:
            if k.startswith(prefix):
                k = k[len(prefix):]
                d[k] = v
        except AttributeError:
            pass

    return d


def map(**kwargs):
    """Returns a dictionary of the given keyword arguments mapped to their
    values from the environment, with input keys lower cased.
    """

    d = {}
    e = lower_dict(environ.copy())

    for k, v in kwargs.items():
        d[k] = e.get(v.lower())

    return d
