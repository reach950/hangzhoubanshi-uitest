#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""智能客服页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AICustomerServicePage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "杭州办事服务客服"')

    # 搜索输入框
    search_textfield_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 搜索按钮
    search_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.width == 28')

    # 输入关键字搜索问题答案
    def search(self, text):
        self.send_keys(self.search_textfield_loc, text)
        self.tap_element(self.search_button_loc)

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 点击默认问题
    def click_default_question(self, question, full=True):
        if full:
            self.click_element_by_name(question)
        else:
            loc = (MobileBy.IOS_PREDICATE,
                   'type == "XCUIElementTypeStaticText" AND name BEGINSWITH "{}"'.format(question))
            self.tap_element(loc)

    # 回复是否显示
    def is_reply_display(self, reply, full=True):
        if full:
            return self.check_element_by_name(reply)
        else:
            loc = (MobileBy.IOS_PREDICATE,
                   'type == "XCUIElementTypeStaticText" AND name BEGINSWITH "{}"'.format(reply))
            return self.is_element_exist_by_loc(loc)
