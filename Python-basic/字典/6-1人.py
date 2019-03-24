#!/usr/bin/env python
# @Time : 2019/3/24 3:29 
__author__ = 'Boaz'

# 使用一个字典来存储一个熟人的信息，包括名、 姓、 年龄 和居住的城市。
# 该字典包含键 first_name, last_name, age 和city。将存储在该字典中的每项信息都打印出来

person = {
    'first_name': 'Taylor',
    'last_name': 'Swift',
    'age': 30,
    'city': 'New York City',
    ('ablum','count'): 5
}
print(person)
for key,values in person.items():
    print(values)

# 喜欢的数字，想出5个人的名字，并用名字作为键， 每个人喜欢的数字作为值来存储。打印每个人的名字和喜欢的数字

favorite={
    'Adam': 23,
    'Elie': 4,
    'David': 7,
    'Van': 13
}

print(favorite['Adam'],favorite['Elie'])