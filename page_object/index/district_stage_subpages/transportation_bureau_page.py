#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""市交通运输局页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class TransportationBureauPage(BasePage):
    # 小客车增量指标
    car_incremental_quota_loc = (MobileBy.ACCESSIBILITY_ID, '小客车增量指标')

    # 打开小客车增量指标页面
    def open_car_incremental_quota_page(self):
        self.tap_element(self.car_incremental_quota_loc)
