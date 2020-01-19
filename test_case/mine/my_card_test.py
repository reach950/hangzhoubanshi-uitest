#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试我的卡包"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step import login


class TestMyCardList(BaseCase):
    """我的-我的证照-证照列表"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_identity_card_page_by_real_name(self):
        """已实名，点击进入居民身份证页面"""
        self.main_page.switch_to_mine_page()
        self.mine_page.open_my_card()
        self.my_card_page.click_identity_card()
        self.assertTrue(self.face_verification_page.is_displayed())

    @login('unreal_name')
    def test_02_open_real_name_authentication_page_by_unreal_name(self):
        """未实名，点击进入实名认证页面"""
        alert_message = '该服务需要实名，请您先完成实名认证！'
        self.main_page.switch_to_mine_page()
        self.mine_page.open_my_card()
        self.mine_page.check_element_by_name(alert_message)
        self.mine_page.click_alert_button(button_lable='确定')
        self.assertTrue(self.real_name_authentication_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
