#!/usr/bin/env python  
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/3 17:34 

import trio

async def async_double(x):
    return 2 * x

print(trio.run(async_double, 3))