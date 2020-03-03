#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""密码管理页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class PasswordManagePage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "密码管理" AND rect.width == 199')

    # 原密码输入框
    old_password_input_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[1]')

    # 新密码输入框
    new_password_input_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[2]')

    # 确认密码输入框
    verify_password_input_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[3]')

    # 确认按钮
    confirm_button = (MobileBy.ACCESSIBILITY_ID, '确认')

    # 修改密码
    def modify_password(self, old_password, new_password):
        self.send_keys(self.old_password_input_loc, old_password)
        self.send_keys(self.new_password_input_loc, new_password)
        self.send_keys(self.verify_password_input_loc, new_password)
        self.tap_element(self.confirm_button)

    # 页面是否消失
    def is_disappeared(self):
        return self.is_element_disappeared_by_loc(self.page_title_loc, exist=False)
