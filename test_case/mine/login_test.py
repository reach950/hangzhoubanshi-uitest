#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试登录"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from config.login_user import login_user


class TestLogin(BaseCase):

    def setUp(self):
        super().setUp()
        self.test_phone_number = login_user['phone_number']
        self.test_identity_number = login_user['identity_number']
        self.test_password = login_user['password']

    def tearDown(self):
        super().tearDown()

    # 测试通过手机号登录
    def test_login_by_phone_number(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.login_page.login(self.test_phone_number, self.test_password)
        self.assertTrue(self.mine_page.is_login())

    # 测试通过身份证号登录
    def test_login_by_identity_number(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.login_page.login(self.test_identity_number, self.test_password)
        self.assertTrue(self.mine_page.is_login())


if __name__ == '__main__':
    unittest.main()
