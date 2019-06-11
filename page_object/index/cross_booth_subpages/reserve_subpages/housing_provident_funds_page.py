#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""公积金页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class HousingProvidentFundsPage(BasePage):

    # 个人住房公积金免缴
    personal_housing_provident_funds_free_loc = (MobileBy.ACCESSIBILITY_ID, '个人住房公积金免缴')

    # 点击个人住房公积金免缴
    def click_personal_housing_provident_funds_free(self):
        self.tap_element(self.personal_housing_provident_funds_free_loc)
