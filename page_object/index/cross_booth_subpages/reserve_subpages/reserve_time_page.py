#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""预约时间页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ReserveTimePage(BasePage):

    # 第一个预约时间
    first_reserve_time_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 点击第一个预约时间
    def click_first_reserve_time(self):
        self.tap_element(self.first_reserve_time_loc)
