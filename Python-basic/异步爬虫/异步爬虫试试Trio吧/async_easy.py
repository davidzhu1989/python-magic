#!/usr/bin/env python
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/4 1:21

# 就是写个简单的 async 的函数

# from time import sleep
import asyncio


async def func1():
    print("func1 start!")
    await asyncio.sleep(2)
    print("func1 exiting")


async def func2():
    print("func2 start!")
    # await sleep(1.5)
    await asyncio.sleep(1.5)
    print("func2 exiting")


async def main():
    print("main start! ")
    await func1()
    await func2()
    print("main over! ")



main()
