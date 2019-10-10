#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试热门应用"""


__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.login import login


class TestAllApps(BaseCase):
    """首页-热门应用-全部"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login(True)
    def test_reduce_app_from_my_apps(self):
        """从我的应用中删除应用"""
        self.index_page.open_all_apps_page()
        reduce_app_name = self.all_apps_page.get_last_app_name_from_my_apps()
        self.all_apps_page.reduce_last_app_from_my_apps()
        self.all_apps_page.back_to_index()
        self.assertFalse(self.index_page.check_element_by_name(reduce_app_name))

    @login(True)
    def test_reduce_app_from_my_apps(self):
        """添加应用到我的应用"""
        self.index_page.open_all_apps_page()
        first_added_app_name = self.all_apps_page.get_first_added_app_name()
        self.all_apps_page.add_app_to_my_apps()
        self.all_apps_page.back_to_index()
        self.assertTrue(self.index_page.check_element_by_name(first_added_app_name))


if __name__ == '__main__':
    unittest.main()
