#!/usr/bin/env python
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/3 17:25

# 一个标准的方法


def regular_double(x):
    return 2 * x

# 一个异步方法


async def async_double(x):
    return 2 * x


# 不能再同步函数里面用 await
# def print_double(x):
#     print(await async_double(x))

