#!/usr/bin/env python
# @Time : 2019/3/27 16:15
__author__ = 'Boaz'

from time import time, sleep


def add(x, y=10):
    return x + y


# if you want to time each of these operations
before = time()
sleep(1.5)
print('add(10)', add(10))
after = time()
print('time taken: ', after-before)

before = time()
sleep(3)
print('add(20, 30)', add(20, 30))
after = time()
print('time taken: ', after-before)

before = time()
sleep(2.5)
print('add("a", "b")', add("a", "b"))
after = time()
print('time taken: ', after-before)