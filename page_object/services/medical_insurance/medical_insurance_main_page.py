#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""医疗保险主页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MedicalInsuranceMainPage(BasePage):
    # 参保查询
    query_insurance_loc = (MobileBy.ACCESSIBILITY_ID, '参保查询')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.query_insurance_loc)
