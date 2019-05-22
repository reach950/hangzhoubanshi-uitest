#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主页"""

__author__ = 'kejie'


from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class IndexPage(BasePage):

    # 我要咨询
    wo_yao_zi_xun = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "bg_up"`]/XCUIElementTypeOther[3]')

    # 办事指南
    ban_shi_zhi_nan = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "bg_up"`]/XCUIElementTypeOther[4]')

    # 打开办事指南页面
    def open_gov_guide_page(self):
        self.tap_element(self.ban_shi_zhi_nan)

    # 打开智能客服页面
    def open_AI_customer_service_page(self):
        self.tap_element(self.wo_yao_zi_xun)
