#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""小客车增量指标页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class CarIncrementalQuotaPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '增量指标')

    # 申请信息
    application_info_loc = (MobileBy.ACCESSIBILITY_ID, '申请信息')

    # 页面是否显示
    def is_display(self):
        page_title = self.find_element(self.page_title_loc)
        application_info = self.find_element(self.application_info_loc)
        if page_title and application_info:
            return page_title.is_displayed() and application_info.is_displayed()
        else:
            return False
