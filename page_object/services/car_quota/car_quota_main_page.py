#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""小客车指标主页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class CarQuotaMainPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "小客车指标" AND rect.width == 199')

    # 增量指标
    incremental_quota_loc = (MobileBy.ACCESSIBILITY_ID, '增量指标')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)
