#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""个人信息页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class UserInfoPage(BasePage):
    # 姓名
    name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[2]'
                                          '/XCUIElementTypeStaticText[2]')

    # 性别
    gender_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[3]'
                                            '/XCUIElementTypeStaticText[2]')

    # 手机号码
    phone_number_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[4]'
                                                  '/XCUIElementTypeStaticText[2]')

    # 身份证号码
    identity_number_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[5]'
                                                     '/XCUIElementTypeStaticText[2]')

    # 实名认证
    real_name_authentication_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[6]')

    # 密码管理
    password_manage_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[7]')

    # 地址管理
    address_manage_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[8]')

    # 获取姓名
    def get_name(self):
        return self.find_element(self.name_loc).get_attribute('value')

    # 获取性别
    def get_gender(self):
        return self.find_element(self.gender_loc).get_attribute('value')

    # 获取手机号码
    def get_phone_number(self):
        return self.find_element(self.phone_number_loc).get_attribute('value')

    # 获取身份证号码
    def get_identity_number(self):
        return self.find_element(self.identity_number_loc).get_attribute('value')

    # 打开地址管理页面
    def open_address_manage_page(self):
        self.tap_element(self.address_manage_loc)

    # 打开密码管理页面
    def open_password_manage_page(self):
        self.tap_element(self.password_manage_loc)

    # 点击实名认证
    def click_real_name_authentication(self):
        self.tap_element(self.real_name_authentication_loc)
