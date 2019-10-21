#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""应用详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ServiceDetailPage(BasePage):
    # 返回页面按钮
    back_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name IN {"back","Nav back"}')

    # 返回上一页
    def back_to_prev_page(self):
        self.tap_element(self.back_button_loc)
