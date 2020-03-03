#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""指南详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class GuideDetailPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '指南详情')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 是否显示事项名称
    def is_item_name_displayed(self, item_name):
        return self.is_element_exist_by_loc(item_name)
