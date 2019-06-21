#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from test_case import login


class LoginPage(BasePage):

    # 用户账号输入框
    username_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 用户密码输入框
    password_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSecureTextField')

    # 登录按钮
    login_button_loc = (MobileBy.ACCESSIBILITY_ID, '立即登录')

    # 登录
    def login(self, username, password):
        # 最后一位数字通过键盘点击输入，不然登录按钮一直为disable状态
        self.send_keys(self.username_input_loc, username[:-1], clear_first=True)
        last_username_number_loc = (MobileBy.ACCESSIBILITY_ID, username[-1])
        self.tap_element(last_username_number_loc)
        self.send_keys(self.password_input_loc, password)
        self.tap_element(self.login_button_loc)
        login.login_state = True
