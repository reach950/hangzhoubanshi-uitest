#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""个人办事指南页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class HandlePersonalAffairsGuidePage(BasePage):

    # 第一个事项
    first_affair_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 第一个事项的名称
    first_affair_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                       '/XCUIElementTypeStaticText[1]')

    # 打开第一个事项指南
    def open_first_affair_guide(self):
        self.tap_element(self.first_affair_loc)

    # 获取第一个事项的名称
    def get_first_affair_name(self):
        return self.find_element(self.first_affair_name_loc).get_attribute('value')
