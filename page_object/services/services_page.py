#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务页"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ServicesPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 345')

    # 交通出行类目
    traffic_category_loc = (MobileBy.ACCESSIBILITY_ID, '交通出行')

    # 户籍办理类目
    residence_registration_category_loc = (MobileBy.ACCESSIBILITY_ID, '户籍办理')

    # 教育类目
    education_category_loc = (MobileBy.ACCESSIBILITY_ID, '教育')

    # 小客车指标图标
    car_quota_image_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeImage" AND rect.x == 126 AND rect.y == 603')

    # 流动人口登记图标
    mobile_population_reside_registration_image_loc = \
        (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeImage" AND rect.x == 126 AND rect.y == 603')

    # 教育缴费图标
    education_pay_image_loc = (MobileBy.IOS_PREDICATE,
                               'type == "XCUIElementTypeImage" AND rect.x == 300 AND rect.y == 347')

    # 打开搜索页面
    def open_search_page(self):
        self.tap_element(self.search_field_loc)

    # 选择交通出行类目
    def select_traffic_category(self):
        self.tap_element(self.traffic_category_loc)

    # 选择户籍办理类目
    def select_residence_registration_category(self):
        self.tap_element(self.residence_registration_category_loc)

    # 选择教育类目
    def select_education_category(self):
        self.tap_element(self.education_category_loc)

    # 点击小客车指标
    def click_car_quota_image(self):
        self.tap_element(self.car_quota_image_loc)

    # 点击流动人口登记
    def click_mobile_population_reside_registration_image(self):
        self.tap_element(self.mobile_population_reside_registration_image_loc)

    # 点击教育缴费
    def click_education_pay_image(self):
        self.tap_element(self.education_pay_image_loc)
