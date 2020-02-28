#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""区县服务主页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class DistrictServicesMainPage(BasePage):
    # 地区选择按钮
    district_select_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.width == 275')

    # 热门应用
    hot_app_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[-1]/XCUIElementTypeStaticText[`name == "热门服务"`]')

    # 热门部门
    hot_departments_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell')

    # 热门部门更多按钮
    hot_departments_more_button_loc = (MobileBy.ACCESSIBILITY_ID, '更多')

    # 市交通运输局
    transportation_bureau_loc = (MobileBy.ACCESSIBILITY_ID, '市交通运输局')

    # 点击地区选择按钮
    def click_district_select_button(self):
        self.tap_element(self.district_select_button_loc)

    # 热门应用是否显示
    def is_hot_app_display(self):
        return self.is_element_exist_by_loc(self.hot_app_loc)

    # 获取所有热门部门
    def get_all_hot_departments(self):
        return self.find_elements(self.hot_departments_loc)

    # 点击热门部门更多按钮
    def click_hot_departments_more_button(self):
        self.tap_element(self.hot_departments_more_button_loc)

    # 点击市交通运输局部门
    def click_transportation_bureau(self):
        self.tap_element(self.transportation_bureau_loc)
