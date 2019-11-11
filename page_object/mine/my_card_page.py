#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的卡包页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MyCardPage(BasePage):
    # 居民身份证
    identity_card_loc = (MobileBy.ACCESSIBILITY_ID, '居民身份证')

    # 点击居民身份证
    def click_identity_card(self):
        self.tap_element(self.identity_card_loc)
