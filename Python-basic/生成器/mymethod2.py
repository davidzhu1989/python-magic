#!/usr/bin/env python
# @Time : 2019/3/30 11:37 
__author__ = 'Boaz'

# 0-100 找出所有的被5整除的数目


def getnum(min_,max_):
    for i in range(min_,max_+1):
        if i % 10 ==0:
            yield i


f = getnum(0, 100)
print(f)
for n in f:
    print(n)