#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""新增投诉建议页面"""

__author__ = 'kejie'

import random
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AddComplaintSuggestionPage(BasePage):
    # 建议选项
    suggestion_choice_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "建议"')

    # 投诉选项
    complaint_choice_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "投诉"')

    # 咨询选项
    consult_choice_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "咨询"')

    # 举报选项
    report_choice_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "举报"')

    # 文字输入框
    text_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')

    # 提交按钮
    submit_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "提 交"')

    # 添加投诉建议
    def add_complaint_suggestion(self, text):
        complaint_type = self._select_random_complaint_type()
        self.send_keys(loc=self.text_input_loc, value=text)
        self.click_element_by_name('完成')
        self.tap_element(self.submit_button_loc)
        return complaint_type

    # 随机选择一个投诉类型
    def _select_random_complaint_type(self):
        num = random.randint(1, 4)
        if num == 1:
            loc = self.suggestion_choice_loc
            type_name = '建议'
        elif num == 2:
            loc = self.complaint_choice_loc
            type_name = '投诉'
        elif num == 3:
            loc = self.consult_choice_loc
            type_name = '咨询'
        else:
            loc = self.report_choice_loc
            type_name = '举报'
        self.tap_element(loc)
        return type_name
