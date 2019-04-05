#!/usr/bin/env python  
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/4 1:02 

import time
import trio


async def broken_double_sleep(x):
    print("*yawn* Going to sleep")
    start_time = time.perf_counter()

    # 没写 await
    # trio.sleep(2 * x)
    # RuntimeWarning: coroutine 'sleep' was never awaited

    await trio.sleep(1.5 * x)

    sleep_time = time.perf_counter() - start_time
    print('Woke up after {:.2f} seconds, feeling well rested!'.format(sleep_time))


trio.run(broken_double_sleep, 3)