#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我要查询页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class QueryPage(BasePage):

    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '我要查询')

    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 搜索按钮
    search_button_loc = (MobileBy.ACCESSIBILITY_ID, 'Search')

    # 热门事项
    hot_items_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "热门事项"')

    # 输入关键字搜索事项
    def search(self, text):
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        hot_items = self.find_element(self.hot_items_loc)
        if page_title and hot_items:
            return page_title.is_displayed() and hot_items.is_displayed()
        else:
            return False
