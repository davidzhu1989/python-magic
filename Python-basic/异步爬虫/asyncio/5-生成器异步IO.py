#!/usr/bin/env python3
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/5 12:16
# 5-生成器异步IO.py

import asyncio

async def mygen(u:int = 10):
    """ Yield powers of 2"""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)


async def main():
    g = [i async for i in mygen()]
    return g


if __name__ == '__main__':

    g = asyncio.run(main())
    print(g)