#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试未实名用户"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.login import Login


def setUpModule():
    Login.unreal_name_user_login()


def tearDownModule():
    Login.real_name_user_login()


class TestMyCard(BaseCase):
    """我的-我的证照-证照列表"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_need_real_name_authentication_to_open_my_card_page(self):
        """未实名，打开我的卡包页面需要实名认证"""
        alert_message = '该服务需要实名，请您先完成实名认证！'
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_card()
        self.assertTrue(self.mine_page.is_alert_message_displayed(alert_message))
        self.mine_page.click_alert_button(button_lable='确定')
        self.assertTrue(self.real_name_authentication_page.is_displayed())


class TestBaseInfo(BaseCase):
    """我的-个人信息-基本信息"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_unreal_user_info(self):
        """未实名用户，姓名，性别，身份证号显示为空"""
        self.main_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        test_name = self.user_info_page.get_name()
        test_gender = self.user_info_page.get_gender()
        test_identity_number = self.user_info_page.get_identity_number()
        self.assertIsNone(test_name)
        self.assertIsNone(test_gender)
        self.assertIsNone(test_identity_number)
        self.user_info_page.click_real_name_authentication()
        self.assertTrue(self.real_name_authentication_page.is_displayed())


if __name__ == '__main__':
    unittest.main()