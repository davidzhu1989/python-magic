#!/usr/bin/env python3
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/7 0:55
# 陷阱时序性和一致性.py.py

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print(f"Hello from {self.getName()}!")
        time.sleep(1)
        print(f"{self.getName()} finished!")


def main():
    for x in range(4):
        mythread = MyThread(name=f"Thread-{x+1}")
        mythread.start()
        # Thread creation is spaced out by at least
        time.sleep(.9)


if __name__ == '__main__':
    main()