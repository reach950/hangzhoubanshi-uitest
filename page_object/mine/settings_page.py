#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""设置页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from test_case.common_test_step import login


class SettingsPage(BasePage):

    # 安全退出按钮
    quit_button_loc = (MobileBy.ACCESSIBILITY_ID, '安全退出')

    # 退出登录按钮
    logout_button_loc = (MobileBy.ACCESSIBILITY_ID, '退出登录')

    # 登出
    def logout(self):
        self.tap_element(self.quit_button_loc)
        self.tap_element(self.logout_button_loc)
        login.login_state = False
