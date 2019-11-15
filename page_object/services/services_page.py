#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务页"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ServicesPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.ACCESSIBILITY_ID, '试试搜索吧')

    # 打开搜索页面
    def open_search_page(self):
        self.tap_element(self.search_field_loc)

    # 滑动到应用所在位置
    def scroll_to_app_location(self, app_name):
        count = 0
        app_loc = (MobileBy.ACCESSIBILITY_ID, app_name)
        while not self.find_element(app_loc, wait=10) or not self.find_element(app_loc).is_displayed():
            if count >= 3:
                break
            self.swipe('up')
            count += 1
