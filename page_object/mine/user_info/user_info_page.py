#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""个人信息页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class UserInfoPage(BasePage):

    # 手机号码
    phone_number_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[4]'
                                                  '/XCUIElementTypeStaticText[2]')

    # 身份证号码
    identity_number_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[5]'
                                                     '/XCUIElementTypeStaticText[2]')

    # 密码管理
    password_manage_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[7]')

    # 地址管理
    address_manage_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[8]')

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
