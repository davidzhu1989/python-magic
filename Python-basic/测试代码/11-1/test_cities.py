#!/usr/bin/env python
# @Time : 2019/3/24 11:20
__author__ = 'Boaz'

import unittest
from city_functions import location


class LoactionTest(unittest.TestCase):
    def test_city_country(self):
        mylocation = location('Santiago', 'Chile')
        self.assertEqual(mylocation, 'Santiago,Chile')
