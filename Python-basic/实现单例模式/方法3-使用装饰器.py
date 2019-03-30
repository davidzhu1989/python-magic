#!/usr/bin/env python
# @Time : 2019/3/30 10:23 
__author__ = 'Boaz'

from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1

class _class():
    pass


one = MyClass()
two = MyClass()

print("one is two? ", one is two)

no1 = _class()
no2 = _class()
print("no1 is no2?", no1 is no2)
print("no1 == no2?", no1 == no2)