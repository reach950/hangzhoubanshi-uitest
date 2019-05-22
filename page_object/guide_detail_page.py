#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""指南详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class GuideDetailPage(BasePage):

    # 页面标题
    page_title = (MobileBy.ACCESSIBILITY_ID, '指南详情')

    # 根据事项名称检查事项的指南详情是否打开
    def check_guide_detail_display_by_name(self, name):
        affair_name_loc = (MobileBy.ACCESSIBILITY_ID, name)
        return self.check_element_by_name(self.page_title) and self.check_element_by_name(affair_name_loc)
