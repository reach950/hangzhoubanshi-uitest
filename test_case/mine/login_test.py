#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试登录"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from config.login_user import real_name_user
from test_case.login import login

test_phone_number = real_name_user['phone_number']
test_identity_number = real_name_user['identity_number']
test_password = real_name_user['password']


class TestLoginByPhoneNumber(BaseCase):
    """我的-登录-手机号登录"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login(False)
    def test_login_by_phone_number_success(self):
        """通过手机号登录成功"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.login_page.login(test_phone_number, test_password)
        self.assertTrue(self.mine_page.is_login())


class TestLoginByIdNumber(BaseCase):
    """我的-登录-身份证号登录"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login(False)
    def test_login_by_identity_number_success(self):
        """通过身份证号登录成功"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.login_page.login(test_identity_number, test_password)
        self.assertTrue(self.mine_page.is_login())


if __name__ == '__main__':
    unittest.main()
