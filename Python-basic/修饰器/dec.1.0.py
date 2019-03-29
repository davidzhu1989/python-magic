#!/usr/bin/env python
# @Time : 2019/3/27 16:27
from time import sleep,time
import random
__author__ = 'Boaz'


# 前面写的太复杂了，把他们写进一个函数, 而且增加了一个减的函数

def add(x, y=10):
    before = time()
    sleep(random.randint(1,2))
    xy = x + y
    after = time()
    print('time taken: ', after-before)
    return xy


def sub(x, y=10):
    return x - y


print('add(10)', add(10))
print('add(20,30)', add(20, 30))
print('add("a", "b")', add("a", "b"))
print('sub(10)', add(10))
print('sub(20,30)', sub(20,30))

# 而且你还是要发现还是要在subtraction里面写一个timer的函数