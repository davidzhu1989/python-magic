#!/usr/bin/env python
# @Time : 2019/3/24 20:17 
__author__ = 'Boaz'

# 编写一个名为Employee的类， 其方法__init__()
# 接受名，姓，和年薪，并将他们存储在属性中
# 编写一个名为 give_raise()的方法。 默认粘性增加 5000 美元，也能够接受其他的年薪增加量


class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase=0):
        if increase > 0:
            self.salary += increase+5000
        else:
            self.salary += 5000
        return self.salary