#!/usr/bin/env python  
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/3 17:36 

# 异步中的等待
import trio


async def double_sleep(x):
    await trio.sleep(2 * x)

trio.run(double_sleep, 3)