#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试地址管理"""

__author__ = 'kejie'

import unittest
from datetime import datetime
from test_case.base_case import BaseCase
from test_case.login import login


class TestAddressManage(BaseCase):

    def setUp(self):
        super().setUp()
        create_time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        self.create_detail_address = '详细地址_{}'.format(create_time_now)
        self.create_username = 'name_{}'.format(create_time_now)
        self.create_phone_number = '133{}'.format(create_time_now[-8:])

    def tearDown(self):
        super().tearDown()

    # 测试地址的增删改
    @login(True)
    def test_create_modify_delete_address(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_address_manage_page()
        self.address_manage_page.click_create_address_button()
        self.update_address_page.update_address(self.create_detail_address, self.create_username,
                                                self.create_phone_number)
        self.assertEqual(self.create_username, self.address_manage_page.get_last_address_username())
        self.assertEqual('{}*****{}'.format(self.create_phone_number[:3], self.create_phone_number[-3:]),
                         self.address_manage_page.get_last_address_phone_number())
        self.assertIn(self.create_detail_address, self.address_manage_page.get_last_address_detail())


if __name__ == '__main__':
    unittest.main()
