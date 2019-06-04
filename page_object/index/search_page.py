#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""搜索页"""

__author__ = 'kejie'


from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class SearchPage(BasePage):

    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSearchField')

    # 搜索按钮
    search_button_loc = (MobileBy.ACCESSIBILITY_ID, 'Search')

    # 输入关键字搜索
    def search(self, text):
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)
