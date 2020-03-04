#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""认证通道页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AuthenticationMethodPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '认证通道')

    # 认证方式
    authentication_method_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[3]'
                                                           '/XCUIElementTypeStaticText[2]')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 获取认证方式
    def get_authentication_method(self):
        return self.find_element(self.authentication_method_loc).get_attribute('name')
