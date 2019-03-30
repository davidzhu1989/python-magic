#!/usr/bin/env python
# @Time : 2019/3/30 14:27 
__author__ = 'Boaz'

# _** 私有变量
# __** 私有方法
# __***__ 系统构造方法


# 参考网址
# https://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html


from os.path import join

class FileObject:
    """ 文件对象的装饰类， 用来保证文件被删除时候正确关闭"""

    def __init__(self, filepath=".", filename='demo.txt'):
        # 读写模式打开 filename文件
        self.file = open(join(filepath,filename),'r+')
        print(self.file.readline())

    def __del__(self):
        self.file.close()
        del self.file

myFile = FileObject()
