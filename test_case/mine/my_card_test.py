#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试我的卡包"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.login import Login
from config.login_users import login_users


class TestMyCardByRealNameUser(BaseCase):
    """我的-我的证照-证照列表-已实名用户"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_identity_card_page_by_real_name(self):
        """已实名，点击进入居民身份证页面"""
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_card()
        self.my_card_page.wait_to_display()
        self.my_card_page.click_identity_card()
        self.assertTrue(self.face_verification_page.is_displayed())


class TestMyCardByUnrealNameUser(BaseCase):
    """我的-我的证照-证照列表-未实名用户"""

    @classmethod
    def setUpClass(cls) -> None:
        unreal_name_user = login_users['unreal_name_user']
        unreal_phone_number = unreal_name_user['phone_number']
        unreal_password = unreal_name_user['password']
        Login.user_logout_without_driver()
        Login.user_login_without_driver(unreal_phone_number, unreal_password)

    @classmethod
    def tearDownClass(cls) -> None:
        real_name_user = login_users['real_name_user']
        real_phone_number = real_name_user['phone_number']
        real_password = real_name_user['password']
        Login.user_logout_without_driver()
        Login.user_login_without_driver(real_phone_number, real_password)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_real_name_authentication_page_by_unreal_name(self):
        """未实名，点击进入实名认证页面"""
        alert_message = '该服务需要实名，请您先完成实名认证！'
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_card()
        self.assertTrue(self.mine_page.is_alert_message_displayed(alert_message))
        self.mine_page.click_alert_button(button_lable='确定')
        self.assertTrue(self.real_name_authentication_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
