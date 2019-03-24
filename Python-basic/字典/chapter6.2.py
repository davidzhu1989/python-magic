#!/usr/bin/env python
# @Time : 2019/3/23 22:25
__author__ = 'Boaz'

# 添加键-值对
alien_0 = dict()
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# 修改字典的值
alien_0['color'] = 'yellow'
print("The alien is now "+ alien_0['color'] + '.')


# This dictionary creation could be rewritten as a dictionary literal