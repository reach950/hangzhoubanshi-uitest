#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""问题求助页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ProblemToSeekHelpPage(BasePage):
    # 常见问题
    frequently_question_loc = (MobileBy.ACCESSIBILITY_ID, '常见问题')

    # 页面是否显示
    def is_displayed(self):
        frequently_question = self.find_element(self.frequently_question_loc)
        if frequently_question:
            return frequently_question.is_displayed()
        else:
            return False
