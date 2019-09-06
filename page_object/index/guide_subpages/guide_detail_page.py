#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""指南详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class GuideDetailPage(BasePage):

    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '指南详情')

    # 根据事项名称检查事项的指南详情是否打开
    def check_guide_detail_display_by_name(self, name):
        item_name_loc = (MobileBy.ACCESSIBILITY_ID, name)
        page_title = self.find_element(self.page_title_loc)
        item_name = self.find_element(item_name_loc)
        if page_title and item_name:
            return page_title.is_displayed() and item_name.is_displayed()
        else:
            return False
