#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""养老保险页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class EndowmentInsurancePage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "养老保险" AND rect.width == 199')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        return True if page_title else False
