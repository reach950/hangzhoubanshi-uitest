#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""地区选择页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class DistrictSelectPage(BasePage):

    # 根据区县名称选择一个区县
    def select_district_by_name(self, district_name):
        district_loc = (MobileBy.ACCESSIBILITY_ID, district_name)
        self.tap_element(district_loc)
