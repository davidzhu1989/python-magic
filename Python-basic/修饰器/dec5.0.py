#!/usr/bin/env python
# @Time : 2019/3/27 17:09
__author__ = 'Boaz'

# 虽然dec4.0已经写的很多了，但是关于参数问题，
# 我们写的不是很完美，所以呢，改成这样
# 把参数这个定义问题交给元素的函数就行


from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        r = func(*args, **kwargs)
        after = time()
        print('time taken: ', after - before)
        return r
    return f


@timer
def add(x, y=10):
    return x + y


@timer
def add3(x, y, z=10):
    return x + y + z


print("add(10)", add(10))
print("add(10,20)", add(10, 20))
print("add3(10,20,30)", add3(10, 20, 30))
