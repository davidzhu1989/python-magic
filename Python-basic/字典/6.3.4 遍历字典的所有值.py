#!/usr/bin/env python
# @Time : 2019/3/24 3:59 
__author__ = 'Boaz'

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

