#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""投诉建议详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ComplaintSuggestionDetailPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '投诉建议详情')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        if page_title:
            return page_title.is_displayed()
        else:
            return False
