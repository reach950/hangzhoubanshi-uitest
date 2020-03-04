#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""激活预约页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ActivateReservePage(BasePage):

    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '激活预约')

    # 取消预约按钮
    cancel_reserve_button_loc = (MobileBy.ACCESSIBILITY_ID, '取消预约')

    # 预约事项
    reserve_item_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage/XCUIElementTypeStaticText[1]')

    # 办事时间
    reserve_time_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage/XCUIElementTypeStaticText[2]')

    # 如何扫码
    how_to_scan_code_loc = (MobileBy.ACCESSIBILITY_ID, '如何扫码')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        if page_title:
            return page_title.is_displayed()
        else:
            return False

    # 取消预约
    def cancel_reserve(self):
        self.tap_element(self.cancel_reserve_button_loc)

    # 获取预约时间
    def get_reserve_time(self):
        return self.find_element(self.reserve_time_loc).get_attribute('name')

    # 获取预约事项名称
    def get_reserve_item_name(self):
        return self.find_element(self.reserve_item_name_loc).get_attribute('name')

    # 打开如何扫码页面
    def open_how_to_scan_code_page(self):
        self.tap_element(self.how_to_scan_code_loc)
