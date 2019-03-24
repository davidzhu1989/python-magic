#!/usr/bin/env python
# @Time : 2019/3/23 22:32 
__author__ = 'Boaz'

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print('Original x-position: '+ str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print(alien_0)
del(alien_0['speed'])
print(alien_0)