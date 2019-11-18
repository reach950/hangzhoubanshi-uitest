#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试个人信息"""

__author__ = 'kejie'

import unittest
import time
from datetime import datetime
from test_case.base_case import BaseCase
from config.login_users import login_users
from test_case.common_test_step.login import login

real_name_user = login_users['real_name_user']
phone_number = real_name_user['phone_number']
identity_number = real_name_user['identity_number']
password = real_name_user['password']
authentication_method = real_name_user['authentication_method']


class TestBaseInfo(BaseCase):
    """我的-个人信息-基本信息"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login('unreal_name')
    def test_01_unreal_user_info(self):
        """未实名用户，姓名，性别，身份证号显示为空"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        test_name = self.user_info_page.get_name()
        test_gender = self.user_info_page.get_gender()
        test_identity_number = self.user_info_page.get_identity_number()
        self.assertIsNone(test_name)
        self.assertIsNone(test_gender)
        self.assertIsNone(test_identity_number)
        self.user_info_page.click_real_name_authentication()
        self.assertTrue(self.real_name_authentication_page.is_displayed())

    @login
    def test_02_real_user_info(self):
        """非银行卡认证用户，显示姓名，性别，身份证号"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        test_name = self.user_info_page.get_name()
        test_gender = self.user_info_page.get_gender()
        test_phone_number = self.user_info_page.get_phone_number()
        test_identity_number = self.user_info_page.get_identity_number()
        self.assertIsNotNone(test_name)
        self.assertIsNotNone(test_gender)
        self.assertEqual('{}*****{}'.format(phone_number[:3], phone_number[-3:]), test_phone_number)
        self.assertEqual('{}*****************{}'.format(identity_number[0], identity_number[-1]),
                         test_identity_number)

    @login
    def test_03_real_user_authentication_method(self):
        """已实名用户可查看实名认证的方式"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.click_real_name_authentication()
        self.assertTrue(self.authentication_method_page.is_displayed())
        self.assertEqual(self.authentication_method_page.get_authentication_method(), authentication_method)


class TestPasswordManage(BaseCase):
    """我的-个人信息-密码管理"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_modify_password_to_old_password(self):
        """修改成原始密码失败"""
        self.index_page.switch_to_mine_page()
        self._modify_password(password, password)
        self.assertFalse(self.login_page.is_displayed())

    @login
    def test_02_modify_password_to_full_letters_or_digits(self):
        """修改成全英文或全数字失败"""
        full_letters = 'hangzhou'
        full_digits = '12345678'
        self.index_page.switch_to_mine_page()
        self._modify_password(password, full_letters)
        self.assertFalse(self.login_page.is_displayed())
        self.password_manage_page.modify_password(password, full_digits)
        self.assertFalse(self.login_page.is_displayed())

    @login
    def test_03_modify_password_to_empty_password(self):
        """修改成全空密码失败"""
        self.index_page.switch_to_mine_page()
        self._modify_password(password, '')
        self.assertFalse(self.login_page.is_displayed())

    @login
    def test_04_modify_password_success(self):
        """修改登录密码成功"""
        new_password = 'test1234'
        self.index_page.switch_to_mine_page()
        self._modify_password(password, new_password)
        self.login_page.login(phone_number, new_password)
        self.assertTrue(self.mine_page.is_login())

        self._modify_password(new_password, password)
        self.login_page.login(phone_number, password)
        self.assertTrue(self.mine_page.is_login())

    def _modify_password(self, old_password, new_password):
        self.mine_page.click_user_area()
        self.user_info_page.open_password_manage_page()
        self.password_manage_page.modify_password(old_password, new_password)


class TestAddressManage(BaseCase):
    """我的-个人信息-地址管理"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_create_address(self):
        """添加地址"""
        create_time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        create_detail_address = '详细地址_{}'.format(create_time_now)
        create_username = 'name_{}'.format(create_time_now)
        create_phone_number = '133{}'.format(create_time_now[-8:])

        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_address_manage_page()
        self.address_manage_page.click_create_address_button()
        self.update_address_page.update_address(create_detail_address, create_username,
                                                create_phone_number)
        time.sleep(3)
        self.assertEqual(create_username, self.address_manage_page.get_last_address_username())
        self.assertEqual('{}*****{}'.format(create_phone_number[:3], create_phone_number[-3:]),
                         self.address_manage_page.get_last_address_phone_number())
        self.assertIn(create_detail_address, self.address_manage_page.get_last_address_detail())

    @login
    def test_02_modify_address(self):
        """修改地址"""
        modify_time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        modify_detail_address = '详细地址_{}'.format(modify_time_now)
        modify_username = 'name_{}'.format(modify_time_now)
        modify_phone_number = '133{}'.format(modify_time_now[-8:])

        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_address_manage_page()
        self.address_manage_page.click_last_address_edit_button()
        self.update_address_page.update_address(modify_detail_address, modify_username,
                                                modify_phone_number)
        time.sleep(3)
        self.assertEqual(modify_username, self.address_manage_page.get_last_address_username())
        self.assertEqual('{}*****{}'.format(modify_phone_number[:3], modify_phone_number[-3:]),
                         self.address_manage_page.get_last_address_phone_number())
        self.assertIn(modify_detail_address, self.address_manage_page.get_last_address_detail())

    @login
    def test_03_delete_address(self):
        """删除地址"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_address_manage_page()
        last_address_username = self.address_manage_page.get_last_address_username()
        last_address_phone_number = self.address_manage_page.get_last_address_phone_number()
        last_address_detail = self.address_manage_page.get_last_address_detail()
        self.address_manage_page.delete_last_address()
        time.sleep(3)
        self.assertNotEqual(last_address_username, self.address_manage_page.get_last_address_username())
        self.assertNotEqual(last_address_phone_number, self.address_manage_page.get_last_address_phone_number())
        self.assertNotEqual(last_address_detail, self.address_manage_page.get_last_address_detail())


if __name__ == '__main__':
    unittest.main()
