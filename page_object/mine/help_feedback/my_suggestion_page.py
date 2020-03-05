#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的建议页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MySuggestionPage(BasePage):
    # 第一条建议的查看详情
    first_suggestion_view_detail_loc = (MobileBy.ACCESSIBILITY_ID, '查看详情')

    # 点击第一条建议的查看详情
    def click_first_suggestion_view_detail(self):
        self.tap_element(self.first_suggestion_view_detail_loc)
