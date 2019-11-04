#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""密码管理页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class PasswordManagePage(BasePage):
    # 原密码输入框
    old_password_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeSecureTextField" AND rect.y == 128')

    # 新密码输入框
    new_password_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeSecureTextField" AND rect.y == 189')

    # 确认密码输入框
    verify_password_input_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeSecureTextField" AND rect.y == 250')

    # 确认按钮
    confirm_button = (MobileBy.ACCESSIBILITY_ID, '确认')

    # 修改密码
    def modify_password(self, old_password, new_password):
        self.send_keys(self.old_password_input_loc, old_password)
        self.send_keys(self.new_password_input_loc, new_password)
        self.send_keys(self.verify_password_input_loc, new_password)
        self.tap_element(self.confirm_button)
