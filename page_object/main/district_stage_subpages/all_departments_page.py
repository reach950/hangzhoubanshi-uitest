#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""全部部门页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AllDepartmentsPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '全部部门')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)
