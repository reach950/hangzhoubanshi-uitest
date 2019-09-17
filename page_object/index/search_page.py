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

    # 客服按钮
    customer_service_button_loc = (MobileBy.ACCESSIBILITY_ID, 'kefu')

    # 取消搜索
    cancel_search_loc = (MobileBy.ACCESSIBILITY_ID, '取消')

    # 热门搜索
    hot_search_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton')

    # 输入关键字搜索
    def search(self, text):
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)

    # 点击客服按钮
    def click_customer_service_button(self):
        self.tap_element(self.customer_service_button_loc)

    # 取消搜索
    def cancel_search(self):
        self.tap_element(self.cancel_search_loc)

    # 获取热门搜索的所有关键词
    def get_all_hot_search_words(self):
        search_words = []
        eles = self.find_elements(self.hot_search_loc)
        for ele in eles:
            search_words.append(ele.get_attribute('name'))
        return search_words
