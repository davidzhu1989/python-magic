#!/usr/bin/env python
# @Time : 2019/3/28 16:11 
__author__ = 'Boaz'

# 定义一个函数找出所有的.py文件路径

import os
import  re
path = '.'
files = os.listdir(path)
print(files)
# regex = re.compile(r"\.py")
for file in files:
    # print(file+"======")
    result = re.search(r'.py$',file)
    if result:
        print(file)