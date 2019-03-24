#!/usr/bin/env python
# @Time : 2019/3/24 20:29 
__author__ = 'Boaz'

import unittest
from myemployee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Scott', 'Joplin',4000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEquals(self.employee.salary, 9000)
        # self.assertEqual(9000, self.employee.give_raise())

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.salary, 5000)
        # self.assertEqual(10000, self.employee.give_raise(1000))