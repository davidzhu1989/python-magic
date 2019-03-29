#!/usr/bin/env python
# @Time : 2019/3/27 16:55 
__author__ = 'Boaz'

from time import time


def timer(func):
    def f(x, y =10):
        before = time()
        result = func(x,y)
        after = time()
        print('time taken: ', after-before)
        return result
    return f


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


add = timer(add)
sub = timer(sub)

print('add(10)', add(10))
print('add(20,30)', add(20, 30))
print('add("A","b")', add("a", "b"))
print('sub(10)', sub(10))
print("sub(20,30)", sub(20, 30))