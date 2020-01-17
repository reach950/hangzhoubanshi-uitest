#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我要预约页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ReservePage(BasePage):

    # 杭州市民中心
    hangzhou_civic_center_loc = (MobileBy.ACCESSIBILITY_ID, '杭州市民中心')

    # 预约信息查询
    query_reserve_info_loc = (MobileBy.ACCESSIBILITY_ID, '预约信息查询')

    # 返回按钮
    back_button_loc = (MobileBy.ACCESSIBILITY_ID, 'back')

    # 打开杭州市民中心页面
    def open_hangzhou_civic_center_page(self):
        self.tap_element(self.hangzhou_civic_center_loc)

    # 打开预约信息查询页面
    def open_query_reserve_info_page(self):
        self.tap_element(self.query_reserve_info_loc)

    # 返回首页
    def back_to_index(self):
        self.tap_element(self.back_button_loc)
