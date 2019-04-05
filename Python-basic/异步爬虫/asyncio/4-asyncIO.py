#!/usr/bin/env python3
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/5 11:10
# 4-asyncIO.py

# 本节将向你介绍一些异步IO自带的可行的脚本设计。

import asyncio
import random
import time


async def randint(a:int, b:int) -> int:
    return random.randint(a, b)

async def partA(n:int) -> str:
    i = await randint(0, 10)
    print(f"partA({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning partA{n} == {result}.")
    return result


async def partB(n:int, arg: str) -> str:
    i = await randint(0, 10)
    print(f"partB({n, arg}) sleeping for {i} seconds")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning partB{n, arg} == {result}")
    return result

async def chain(n:int) -> None:
    start = time.perf_counter()
    p1 = await partA(n)
    p2 = await partB(n, p1)
    end = time.perf_counter()-start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == '__main__':
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")



