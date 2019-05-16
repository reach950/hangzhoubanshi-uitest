#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主页"""

__author__ = 'kejie'


from page_object.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class IndexPage(BasePage):

    # 小客车指标
    quota_of_car = (MobileBy.ACCESSIBILITY_ID, '小客车指标')

    # 打开小客车指标页面
    def open_quota_of_car_page(self):
        self.tap_element(self.quota_of_car)
