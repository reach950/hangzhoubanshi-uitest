#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试全部应用"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestAllApps(BaseCase):

    def setUp(self):
        super().setUp()
        self.name = '全部应用'

    def tearDown(self):
        super().tearDown()

    # 测试打开全部应用
    def test_open_all_apps_page(self):
        self.index_page.open_all_apps_page()
        self.all_apps_page.check_element_by_name(self.name)


if __name__ == '__main__':
    unittest.main()
