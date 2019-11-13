#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""建议详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class SuggestionDetailPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '建议记录')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        if page_title:
            return page_title.is_displayed()
        else:
            return False
