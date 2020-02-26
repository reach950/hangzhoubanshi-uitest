#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""办事指南选择页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class GuideSelectPage(BasePage):
    # 个人办事
    personal_loc = (MobileBy.ACCESSIBILITY_ID, 'img Personal')

    # 法人办事
    legal_loc = (MobileBy.ACCESSIBILITY_ID, 'img legal')

    # 进入个人办事页面
    def click_personal_guide(self):
        self.tap_element(self.personal_loc)

    # 进入法人办事页面
    def click_legal_guide(self):
        self.tap_element(self.legal_loc)
