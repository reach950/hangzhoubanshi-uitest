#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""更新地址页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class UpdateAddressPage(BasePage):
    # 简要地址输入框
    brief_address_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField" AND rect.y == 88')

    # 详细地址输入框
    detail_address_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField" AND rect.y == 132')

    # 姓名输入框
    username_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField" AND rect.y == 176')

    # 手机号码输入框
    phone_number_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField" AND rect.y == 220')

    # 保存按钮
    save_button_loc = (MobileBy.ACCESSIBILITY_ID, '保存')

    # 简要地址选项列表第一个选项
    first_option_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeCell" AND rect.y == 449')

    # 更新地址
    def update_address(self, detail_address, username, phone_number):
        self.tap_element(self.brief_address_input_loc)
        for _ in range(3):
            self.tap_element(self.first_option_loc)
        self.send_keys(self.detail_address_input_loc, detail_address, clear_first=True)
        self.send_keys(self.username_input_loc, username, clear_first=True)
        self.send_keys(self.phone_number_input_loc, phone_number, clear_first=True)
        self.tap_element(self.save_button_loc)
