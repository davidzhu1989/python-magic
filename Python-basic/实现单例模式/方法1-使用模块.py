#!/usr/bin/env python
# @Time : 2019/3/30 10:07 
__author__ = 'Boaz'


# 使用模块就可以实现单利模式了？
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()


# 将上面代码保存到 testsingle.py中
# 然后 这样使用

#
# from testsingle import my_singleton
#
# my_singleton.foo()
#
# 就可以使用foo()这个函数了