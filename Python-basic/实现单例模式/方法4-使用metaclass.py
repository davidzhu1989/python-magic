#!/usr/bin/env python
# @Time : 2019/3/30 11:15
__author__ = 'Boaz'

# 元类(metclass) 可以控制类的创建过程，
# 1. 拦截类的创建
# 2. 修改类的定义
# 3. 返回修改后的类


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Myclass(metaclass=Singleton):
    pass


class ClassB():
    pass


one = Myclass()
two = Myclass()
print("one is two? ", one is two)
oneB = ClassB()
twoB = ClassB()
print("oneB is twoB ?", oneB is twoB)