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

    # 小客车指标
    car_quota_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView'
                                               '/XCUIElementTypeCell[7]/XCUIElementTypeOther/XCUIElementTypeImage')

    # 流动人口登记
    mobile_population_reside_registration_loc = (MobileBy.IOS_CLASS_CHAIN,
                                                 '**/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]'
                                                 '/XCUIElementTypeOther/XCUIElementTypeImage')

    # 教育缴费
    education_pay_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView'
                                                   '/XCUIElementTypeCell[5]/XCUIElementTypeOther/XCUIElementTypeImage')

    # 点击搜索框
    def click_search_field(self):
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
    def click_car_quota(self):
        self.tap_element(self.car_quota_loc)

    # 点击流动人口登记
    def click_mobile_population_reside_registration(self):
        self.tap_element(self.mobile_population_reside_registration_loc)

    # 点击教育缴费
    def click_education_pay(self):
        self.tap_element(self.education_pay_loc)
