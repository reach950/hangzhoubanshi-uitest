#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的卡包页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MyCardPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "我的卡包" AND rect.width == 199')

    # 居民身份证
    identity_card_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 点击居民身份证
    def click_identity_card(self):
        self.tap_element(self.identity_card_loc)

    # 等到页面显示
    def wait_to_display(self):
        self.is_element_exist_by_loc(self.page_title_loc)
