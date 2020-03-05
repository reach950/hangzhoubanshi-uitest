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
    department_complaint_choice_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "部门建议投诉"')

    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "投诉建议" AND rect.width == 199')

    # 点击添加部门投诉建议
    def click_add_department_complaint_suggestion(self):
        self.tap_element(self.add_complaint_suggestion_button_loc)
        self.tap_element(self.department_complaint_choice_loc)

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 通过投诉类型点击第一条投诉建议
    def click_first_complaint_by_complaint_type(self, type_name):
        self.click_element_by_name(type_name)
