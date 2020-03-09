#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试未登录用户"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.login import Login


class TestGuestUser(BaseCase):
    """未登录用户"""

    @classmethod
    def setUpClass(cls) -> None:
        Login.user_logout()

    @classmethod
    def tearDownClass(cls) -> None:
        Login.real_name_user_login()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_guest_user_has_no_search_history(self):
        """首页-搜索-文字搜索-未登录用户没有历史搜索"""
        search_text = '公积金'
        self.main_page.click_search_field()
        self.search_page.search(search_text)
        self.search_page.click_close_search_image()
        self.assertTrue(self.search_page.is_search_history_disappeared())


if __name__ == '__main__':
    unittest.main()
