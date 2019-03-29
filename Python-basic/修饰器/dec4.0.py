#!/usr/bin/env python
# @Time : 2019/3/27 17:02 
__author__ = 'Boaz'

from time import time

# so we use decorators!
# 想要用的话自己直接写就OK了


def timer(func):
    def f(x,y=10):
        before = time()
        r = x + y
        after = time()
        print('token time: ', after-before)
        return r
    return f


@timer
def add(x, y):
    return x+y

print(add(10,20))
# 现在他就有了timer的功能了
# 只是不想让你写成 add = timer(add)