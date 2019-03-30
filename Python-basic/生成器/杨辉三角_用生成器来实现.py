#!/usr/bin/env python
# @Time : 2019/3/30 11:42 
__author__ = 'Boaz'

# 杨辉三角，试着写一个generator，不断输出下一行的 list

def triangles(n):
    # L = [1]
    # while True:
    #     yield L
    #     L = [L[x]+L[x+1] for x in range(len(L)-1)]
    #     L.insert(0,1)
    #     L.append(1)
    #     if len(L)>10:
    #         break

    L = [1]
    while True:
        yield L
        L = [L[x]+L[x+1]for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        if len(L)>n:
            break

a = triangles(10)
for i in a:
    print(i)