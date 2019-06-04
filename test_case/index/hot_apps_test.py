#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试热门应用"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestHotApps(BaseCase):

    def setUp(self):
        super().setUp()
        self.name = '全部应用'

    def tearDown(self):
        super().tearDown()

    # 测试打开全部应用
    def test_open_all_apps_page(self):
        self.index_page.open_all_apps_page()
        self.assertTrue(self.all_apps_page.check_element_by_name(self.name), '点击更多打开全部页面失败')


if __name__ == '__main__':
    unittest.main()
