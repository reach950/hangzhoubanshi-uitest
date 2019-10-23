#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""区县服务主页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class DistrictServicesIndexPage(BasePage):
    # 地区选择按钮
    district_select_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.width == 275')

    # 热门应用
    hot_app_loc = (MobileBy.ACCESSIBILITY_ID, '下城1call')

    # 热门部门
    hot_departments_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell')

    # 热门部门更多按钮
    hot_departments_more_button_loc = (MobileBy.ACCESSIBILITY_ID, '更多')

    # 打开地区选择页面
    def open_district_select_page(self):
        self.tap_element(self.district_select_button_loc)

    # 热门应用是否显示
    def is_hot_app_display(self):
        hot_app = self.find_element(self.hot_app_loc)
        if hot_app:
            return hot_app.is_displayed()
        else:
            return False

    # 获取所有热门部门
    def get_all_hot_departments(self):
        return self.find_elements(self.hot_departments_loc)

    # 打开全部部门页面
    def open_all_departments_page(self):
        self.tap_element(self.hot_departments_more_button_loc)
