#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试登录"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from config.login_users import login_users
from common_test_step.login import Login

real_name_user = login_users['real_name_user']
test_phone_number = real_name_user['phone_number']
test_identity_number = real_name_user['identity_number']
test_password = real_name_user['password']
login_failed_alert_message = '不存在的手机号/身份证，请您先注册！'


class TestLoginByPhoneNumber(BaseCase):
    """我的-登录-手机号登录"""

    @classmethod
    def setUpClass(cls) -> None:
        Login.user_logout_without_driver()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_login_failed_by_phone_number_not_register(self):
        """登录失败，手机号未注册"""
        not_register_phone_number = '15812346789'
        Login.user_login(self.driver, username=not_register_phone_number, password=test_password)
        self.login_page.check_element_by_name(login_failed_alert_message)

    def test_02_login_by_phone_number_success(self):
        """通过手机号登录成功"""
        Login.user_login(self.driver, username=test_phone_number, password=test_password)
        self.assertTrue(self.mine_page.is_login())


class TestLoginByIdNumber(BaseCase):
    """我的-登录-身份证号登录"""

    @classmethod
    def setUpClass(cls) -> None:
        Login.user_logout_without_driver()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_login_failed_by_identity_number_not_register(self):
        """登录失败，身份证未注册"""
        not_register_identity_number = '421127198812120007'
        Login.user_login(self.driver, username=not_register_identity_number, password=test_password)
        self.login_page.check_element_by_name(login_failed_alert_message)

    def test_02_login_by_identity_number_success(self):
        """通过身份证号登录成功"""
        Login.user_login(self.driver, username=test_identity_number, password=test_password)
        self.assertTrue(self.mine_page.is_login())


if __name__ == '__main__':
    unittest.main()
