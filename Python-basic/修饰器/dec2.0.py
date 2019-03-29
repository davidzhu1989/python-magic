#!/usr/bin/env python
# @Time : 2019/3/27 16:36
import time

__author__ = 'Boaz'

# 但是前面的 add 和 sub 都是函数， 把函数当作一个参数，写在timer的函数里面


def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def timer(func, x, y=10):
    before = time.time()
    result = func(x,y)
    after = time.time()
    print('time taken: ', round((after-before)))
    return result


print('add(10)', timer(add,10,20))

# 但是这个10 这个参数 对计时器来说是无关的，所以还是要修改一下
