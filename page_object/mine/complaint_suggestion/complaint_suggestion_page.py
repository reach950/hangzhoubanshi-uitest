#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""投诉建议页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ComplaintSuggestionPage(BasePage):
    # 添加投诉建议按钮
    add_complaint_suggestion_button_loc = (MobileBy.ACCESSIBILITY_ID, '+ 添加投诉建议')

    # 部门建议投诉选择项
    complaint_choice_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "部门建议投诉"')

    # 打开添加投诉建议页面
    def open_add_complaint_suggestion_page(self):
        self.tap_element(self.add_complaint_suggestion_button_loc)
        self.tap_element(self.complaint_choice_loc)
