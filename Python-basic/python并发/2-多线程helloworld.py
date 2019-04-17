#!/usr/bin/env python3
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/6 14:20
# 2-多线程helloworld.py

import threading
import time


def hello_world():
    print(f"hello from {threading.get_ident()}")


t1 = threading.Thread(target=hello_world)
t2 = threading.Thread(target=hello_world)

t1.start()
t2.start()