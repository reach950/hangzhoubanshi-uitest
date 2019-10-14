#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""杭州市民中心页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class HangzhouCivicCenterPage(BasePage):

    # 公积金
    housing_provident_funds_loc = (MobileBy.ACCESSIBILITY_ID, '公积金')

    # 打开公积金页面
    def open_housing_provident_funds_page(self):
        self.tap_element(self.housing_provident_funds_loc)
