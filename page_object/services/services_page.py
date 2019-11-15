#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务页"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ServicesPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.ACCESSIBILITY_ID, '试试搜索吧')

    # 交通出行类目
    traffic_category_loc = (MobileBy.ACCESSIBILITY_ID, '交通出行')

    # 户籍办理类目
    residence_registration_category_loc = (MobileBy.ACCESSIBILITY_ID, '户籍办理')

    # 教育类目
    education_category_loc = (MobileBy.ACCESSIBILITY_ID, '教育')

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
