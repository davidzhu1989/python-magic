#!/usr/bin/env python
# @Time : 2019/3/30 10:11 
__author__ = 'Boaz'

import unittest

class Singletonbase(object):
    """
    为了使某个类只能出现一个实例
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singletonbase, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(Singletonbase):
    a = 12343234234234234234234234234212312


one = Myclass()
two = Myclass()

print(one == two)

print("one is two: ", one is two)

print("id(one){}, id(two){}".format(id(one),id(two)))