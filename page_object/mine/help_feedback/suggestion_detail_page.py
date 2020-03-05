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
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 处理状态是否显示
    def is_handle_status_displayed(self, status):
        return self.is_element_exist_by_name(status)

    # 建议类型是否显示
    def is_suggestion_type_displayed(self, suggestion_type):
        return self.is_element_exist_by_name(suggestion_type)

    # 建议内容是否显示
    def is_suggestion_content_displayed(self, content):
        return self.is_element_exist_by_name(content)
