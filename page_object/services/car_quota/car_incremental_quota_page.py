#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""小客车增量指标页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class CarIncrementalQuotaPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "增量指标" AND rect.width == 199')

    # 申请信息
    application_info_loc = (MobileBy.ACCESSIBILITY_ID, '申请信息')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)
