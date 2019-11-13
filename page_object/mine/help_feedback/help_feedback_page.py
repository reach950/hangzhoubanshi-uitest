#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""求助反馈页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class HelpFeedbackPage(BasePage):
    # 问题求助
    problem_to_seek_help_loc = (MobileBy.ACCESSIBILITY_ID, '问题求助')

    # App意见反馈
    feedback_loc = (MobileBy.ACCESSIBILITY_ID, 'App意见反馈')

    # 我的建议
    my_suggestion_loc = (MobileBy.ACCESSIBILITY_ID, '我的建议')

    # 打开问题求助
    def open_problem_to_seek_help(self):
        self.tap_element(self.problem_to_seek_help_loc)

    # 打开意见反馈
    def open_feedback(self):
        self.tap_element(self.feedback_loc)

    # 打开我的建议
    def open_my_suggestion(self):
        self.tap_element(self.my_suggestion_loc)
