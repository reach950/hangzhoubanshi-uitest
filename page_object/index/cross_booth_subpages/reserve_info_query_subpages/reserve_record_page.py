#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""预约记录页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ReserveRecordPage(BasePage):

    # 第一条预约记录
    first_reserve_record_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 第一条预约记录的预约状态
    first_reserve_record_state_loc = (MobileBy.IOS_CLASS_CHAIN,
                                      '**/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[5]')

    # 打开第一条预约详情
    def open_first_reserve_detail_page(self):
        self.tap_element(self.first_reserve_record_loc)

    # 获取第一条预约状态
    def get_first_reserve_record_state(self):
        return self.find_element(self.first_reserve_record_state_loc).get_attribute('value')
