#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class LoginPage(BasePage):

    # 用户账号输入框
    username_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 用户密码输入框
    password_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSecureTextField')

    # 登录按钮
    login_button_loc = (MobileBy.ACCESSIBILITY_ID, '立即登录')

    # 登录
    def login(self, username, password):
        self.send_keys(self.username_input_loc, username)
        self.send_keys(self.password_input_loc, password)
        self.tap_element(self.login_button_loc)
