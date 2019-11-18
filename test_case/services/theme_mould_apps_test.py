#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试主题模版应用"""

__author__ = 'kejie'

import unittest
import time
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestThemeApps(BaseCase):
    """服务-主题模版应用-主题应用"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_car_quota_success(self):
        """打开小客车指标应用成功"""
        app_name = '小客车指标'
        self.index_page.switch_to_services_page()
        self.services_page.select_traffic_category()
        self.services_page.click_element_by_name(app_name)
        self.assertTrue(self.car_quota_index_page.is_displayed())

    @login
    def test_02_open_mobile_population_registration_success(self):
        """打开流动人口登记应用成功"""
        app_name = '流动人口登记'
        self.index_page.switch_to_services_page()
        self.services_page.select_residence_registration_category()
        self.services_page.click_element_by_name(app_name)
        self.assertTrue(self.mobile_population_reside_registration_page.is_displayed())

    @login
    def test_03_open_medical_insurance_success(self):
        """打开医疗保险应用成功"""
        app_name = '医疗保险'
        self.index_page.open_all_apps_page()
        time.sleep(3)
        self.all_apps_page.scroll_to_app_location(app_name)
        self.all_apps_page.click_element_by_name(app_name)
        self.assertTrue(self.medical_insurance_index_page.is_displayed())

    @login
    def test_04_open_education_pay_success(self):
        """打开教育缴费应用成功"""
        app_name = '教育缴费'
        self.index_page.switch_to_services_page()
        self.services_page.select_education_category()
        self.services_page.click_element_by_name(app_name)
        self.assertTrue(self.common_pay_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
