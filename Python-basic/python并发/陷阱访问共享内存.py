#!/usr/bin/env python3
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/7 0:59
# 陷阱访问共享内存.py

import threading
import time


class Counter():
    def __init__(self):
        self.count = 0

    def increment_until_100(self):
        while self.count != 100:
            print(f"{threading.current_thread().getName()} incrementing.")
            self.count += 1
            time.sleep(1)


def worker(counter):
    counter.increment_until_100()


def main():
    counter = Counter()
    for x in range(7):
        count_thread = threading.Thread(
            name=f"Thread-{x+1}",
            args=[counter],
            target=worker,
        )
        count_thread.start()
        time.sleep(.9)

    print(f"Counter final value is {counter.count}")


if __name__ == '__main__':
    main()