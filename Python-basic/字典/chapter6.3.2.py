#!/usr/bin/env python
# @Time : 2019/3/24 3:53 
__author__ = 'Boaz'

# 遍历字典所有的键

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print('Hi '+name.title()+", I see your favorite language is "+ favorite_languages[name].title()+"!")



