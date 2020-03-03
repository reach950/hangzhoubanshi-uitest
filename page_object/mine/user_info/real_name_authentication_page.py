#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""实名认证页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class RealNameAuthenticationPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "实名认证" AND rect.width == 199')

    # 支付宝验证
    alipay_loc = (MobileBy.ACCESSIBILITY_ID, '支付宝验证')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)
