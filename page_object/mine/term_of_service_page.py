#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务条款页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class TermOfServicePage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '服务协议')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)
