#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""意见反馈页面"""

__author__ = 'kejie'

import random
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class FeedbackPage(BasePage):
    # 功能异常
    dysfunction_loc = (MobileBy.ACCESSIBILITY_ID, '功能异常：功能不能用')

    # 产品建议
    product_proposal_loc = (MobileBy.ACCESSIBILITY_ID, '产品建议：用的不好，提提建议')

    # 安全问题
    security_problem_loc = (MobileBy.ACCESSIBILITY_ID, '安全问题：密码、隐私、欺诈等')

    # 行政办事异常
    handle_item_exception_loc = (MobileBy.ACCESSIBILITY_ID, '行政办事异常：加载进程慢、无法办理')

    # 其他问题
    other_problem_loc = (MobileBy.ACCESSIBILITY_ID, '其他问题')

    # 文字输入框
    text_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')

    # 提交按钮
    submit_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "提交"')

    # 随机选择一个问题类型
    def select_random_problem_type(self):
        num = random.randint(1, 5)
        if num == 1:
            loc = self.dysfunction_loc
        elif num == 2:
            loc = self.product_proposal_loc
        elif num == 3:
            loc = self.security_problem_loc
        elif num == 4:
            loc = self.handle_item_exception_loc
        else:
            loc = self.other_problem_loc
        self.tap_element(loc)
        return loc[1]

    # 输入问题描述文本
    def input_text(self, text):
        self.send_keys(loc=self.text_input_loc, value=text)
        self.click_element_by_name('完成')

    # 提交按钮是否可以点击
    def is_submit_button_enabled(self):
        is_enabled = self.find_element(self.submit_button_loc).get_attribute('enabled')
        if is_enabled == 'true':
            return True
        else:
            return False

    # 滑动到页面底部
    def scroll_to_footer(self):
        self.swipe('up')

    # 点击提交按钮
    def click_submit_button(self):
        self.tap_element(self.submit_button_loc)
