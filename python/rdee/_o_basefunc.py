#!/usr/bin/env python3
# coding=utf-8


from typing import Sequence

def singleton(orig_cls):
    """
    A functional decorator for implementing singleton coding protocol.
    Code is copied from https://igeorgiev.eu/python/design-patterns/python-singleton-pattern-decorator/
    :param orig_cls: origincal class, since it is used to decorate a class
    """
    #@sk <local-import/>
    from functools import wraps

    #@sk <store desciption="store the single instance and orginal new method">
    orig_new = orig_cls.__new__
    instance = None

    #@sk <wrap-new/>
    @wraps(orig_cls.__new__)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = orig_new(cls, *args, **kwargs)
        return instance
    orig_cls.__new__ = __new__

    #@sk <return/>
    return orig_cls


def is_sequence(obj):
    return isinstance(obj, Sequence) and not isinstance(obj, str)


def isinstanceAll(seq: Sequence, targetType):
    if not is_sequence(seq):
        raise TypeError
    for ele in seq:
        if not isinstance(ele, targetType):
            return False
    return True