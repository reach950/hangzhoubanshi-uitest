#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试个人信息"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from config.login_user import login_user
from test_case.login import login


class TestUserInfo(BaseCase):

    def setUp(self):
        super().setUp()
        self.phone_number = login_user['phone_number']
        self.identity_number = login_user['identity_number']
        self.password = login_user['password']

    def tearDown(self):
        super().tearDown()

    # 测试个人信息内容
    @login(True)
    def test_get_user_info(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        test_phone_number = self.user_info_page.get_phone_number()
        test_identity_number = self.user_info_page.get_identity_number()
        self.assertEqual('{}*****{}'.format(self.phone_number[:3], self.phone_number[-3:]), test_phone_number)
        self.assertEqual('{}*********{}'.format(self.identity_number[0], self.identity_number[-1]),
                         test_identity_number)

    # 测试修改登录密码
    @login(True)
    def test_modify_password(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_password_manage_page()
        self.password_manage_page.modify_password()


if __name__ == '__main__':
    unittest.main()
