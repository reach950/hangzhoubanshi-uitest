#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试热门应用"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestAllApps(BaseCase):
    """首页-热门应用-热门应用与全部"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_reduce_app_from_my_apps(self):
        """从我的应用中删除应用"""
        self.index_page.open_all_apps_page()
        self.all_apps_page.click_edit_button()
        last_app_before_delete = self.all_apps_page.get_last_app_name_from_my_apps()
        self.all_apps_page.delete_last_app_from_my_apps()
        last_app_after_delete = self.all_apps_page.get_last_app_name_from_my_apps()
        self.assertNotEqual(last_app_before_delete, last_app_after_delete)
        self.all_apps_page.click_finish_button()
        self.all_apps_page.back_to_index()
        self.assertFalse(self.index_page.check_element_by_name(last_app_before_delete))

    @login
    def test_02_add_app_from_my_apps(self):
        """添加应用到我的应用"""
        self.index_page.open_all_apps_page()
        self.all_apps_page.click_edit_button()
        last_app_before_add = self.all_apps_page.get_last_app_name_from_my_apps()
        self.all_apps_page.add_first_app_to_my_apps()
        last_app_after_add = self.all_apps_page.get_last_app_name_from_my_apps()
        self.assertNotEqual(last_app_before_add, last_app_after_add)
        self.all_apps_page.click_finish_button()
        self.all_apps_page.back_to_index()
        self.assertTrue(self.index_page.check_element_by_name(last_app_after_add))


if __name__ == '__main__':
    unittest.main()
