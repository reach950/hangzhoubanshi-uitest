#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""小客车指标主页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class CarQuotaIndexPage(BasePage):
    # 增量指标
    incremental_quota_loc = (MobileBy.ACCESSIBILITY_ID, '增量指标')

    # 页面是否显示
    def is_displayed(self):
        incremental_quota = self.find_element(self.incremental_quota_loc)
        if incremental_quota:
            return incremental_quota.is_displayed()
        else:
            return False
