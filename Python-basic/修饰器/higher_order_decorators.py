#!/usr/bin/env python
# @Time : 2019/3/27 17:25 
__author__ = 'Boaz'

#可以嵌套更多的装饰器


def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                rv = f(*args,**kwargs)
            return rv
        return wrapper
    return inner


@ntimes(3)
def add(x,y):
    print(x+y)
    return x+y

add(3,5)