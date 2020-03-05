#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""问题求助页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ProblemToSeekHelpPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "问题求助" AND rect.width == 199')

    # 等到页面显示
    def wait_to_display(self):
        self.is_element_exist_by_loc(self.page_title_loc)

    # 点击问题
    def click_question(self, question):
        self.click_element_by_name(question)

    # 问题回复是否显示
    def is_reply_displayed(self, reply):
        return self.is_element_exist_by_name(reply)

    # 问题回复是否消失
    def is_reply_disappeared(self, reply):
        return self.is_element_disappeared_by_name(reply, exist=False)
