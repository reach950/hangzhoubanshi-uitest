#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""市交通运输局页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class TransportationBureauPage(BasePage):
    # 小客车增量指标
    car_incremental_quota_loc = (MobileBy.ACCESSIBILITY_ID, '小客车增量指标')

    # 点击小客车增量指标
    def click_car_incremental_quota(self):
        self.tap_element(self.car_incremental_quota_loc)
