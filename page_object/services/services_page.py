#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务页"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ServicesPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSearchField')

    # 所有应用
    all_apps_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell'
                                              '/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 打开搜索页面
    def open_search_page(self):
        self.tap_element(self.search_field_loc)

    # 获取所有应用
    def get_all_apps(self):
        return self.find_elements(self.all_apps_loc)
