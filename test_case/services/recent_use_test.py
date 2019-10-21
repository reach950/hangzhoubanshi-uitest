#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试服务页面最近使用"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestRecentUse(BaseCase):
    """服务-最近使用-最近使用应用"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_sort_by_open_app_in_recent_use(self):
        """打开最近使用下的应用，重新排序"""
        self.index_page.switch_to_services_page()
        last_recent_use_app_name = self.services_page.get_last_recent_use_app_name()
        self.services_page.open_last_recent_use_app()
        self.service_detail_page.back_to_prev_page()
        # 最近使用的最后一个应用重新排序到了第一个
        self.assertEqual(self.services_page.get_first_recent_use_app_name(), last_recent_use_app_name)

    @login
    def test_02_sort_by_open_app_not_in_recent_use(self):
        """打开非最近使用下的应用，重新排序"""
        self.index_page.switch_to_services_page()
        not_recent_use_app_name = self.services_page.open_not_recent_use_app_and_return_app_name()
        self.service_detail_page.back_to_prev_page()
        # 非最近使用的应用重新排序到了最近使用第一个
        self.assertEqual(self.services_page.get_first_recent_use_app_name(), not_recent_use_app_name)


if __name__ == '__main__':
    unittest.main()
