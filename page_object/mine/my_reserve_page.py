#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的预约页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MyReservePage(BasePage):
    # 行政预约
    government_reserve_loc = (MobileBy.ACCESSIBILITY_ID, '行政预约')

    # 医疗预约
    medical_reserve_loc = (MobileBy.ACCESSIBILITY_ID, '医疗预约')

    # 第一条预约记录日期
    first_reserve_date_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                        '/XCUIElementTypeStaticText[1]')

    # 第一条预约记录地址
    first_reserve_address_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                           '/XCUIElementTypeStaticText[2]')

    # 第一条预约记录名称
    first_reserve_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                        '/XCUIElementTypeStaticText[3]')

    # 获取第一条预约记录日期
    def get_first_reserve_date(self):
        return self.find_element(self.first_reserve_date_loc).get_attribute('name')

    # 获取第一条预约记录地址
    def get_first_reserve_address(self):
        return self.find_element(self.first_reserve_address_loc).get_attribute('name')

    # 获取第一条预约记录名称
    def get_first_reserve_name(self):
        return self.find_element(self.first_reserve_name_loc).get_attribute('name')
