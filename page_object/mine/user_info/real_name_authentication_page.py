#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""实名认证页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class RealNameAuthenticationPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '实名认证')

    # 支付宝验证
    alipay_loc = (MobileBy.ACCESSIBILITY_ID, '支付宝验证')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        alipay = self.find_element(self.alipay_loc)
        if page_title and alipay:
            return page_title.is_displayed() and alipay.is_displayed()
        else:
            return False
