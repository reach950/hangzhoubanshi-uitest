#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""流动人口居住登记页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MobilePopulationResideRegistrationPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '流动人口居住登记')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        return True if page_title else False
