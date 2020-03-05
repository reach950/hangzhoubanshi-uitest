#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试个人信息"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestBaseInfoByUnrealNameUser(BaseCase):
    """我的-个人信息-基本信息-未实名用户"""

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
