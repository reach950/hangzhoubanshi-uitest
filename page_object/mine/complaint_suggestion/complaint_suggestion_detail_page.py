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
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 投诉内容是否显示
    def is_contain_complaint_content(self, complaint_content):
        return self.is_element_exist_by_name(complaint_content)
