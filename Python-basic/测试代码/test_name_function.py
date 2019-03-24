#!/usr/bin/env python
# @Time : 2019/3/24 5:43 
__author__ = 'Boaz'

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """
    测试 name_function.py
    """
    def test_first_last_name(self):
        """
        能够处理 Jains Joplin这样的名字吗？？？？
        :return:
        """
        formatted_name = get_formatted_name('jains1', 'joplin')
        self.assertEqual(formatted_name, 'Jains1 Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

