#!/usr/bin/env python
# @Time : 2019/3/24 5:35 
__author__ = 'Boaz'

from name_function import get_formatted_name

print('Enter "q" at any time to quit')
while True:
    first = input('\nPlease give me first name: ')
    if first == 'q':
        break
    last = input("please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('\tNeatly formatted name: '+ formatted_name+'.')
