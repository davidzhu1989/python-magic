#!/usr/bin/env python
# @Time : 2019/3/24 3:57 
__author__ = 'Boaz'

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(name.title()+', Thank you for taking the poll.')

# 就是有个sorted()函数处理好就🆗了