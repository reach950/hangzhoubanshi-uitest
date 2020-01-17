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
        self.main_page.switch_to_services_page()
        self.services_page.select_traffic_category()
        self.services_page.click_car_quota_image()
        self.assertTrue(self.car_quota_main_page.is_displayed())

    @login
    def test_02_open_mobile_population_registration_success(self):
        """打开流动人口登记应用成功"""
        self.main_page.switch_to_services_page()
        self.services_page.select_residence_registration_category()
        self.services_page.click_mobile_population_reside_registration_image()
        self.assertTrue(self.mobile_population_reside_registration_page.is_displayed())

    @unittest.skip
    @login
    def test_03_open_medical_insurance_success(self):
        """打开医疗保险应用成功"""
        app_name = '医疗保险'
        self.main_page.switch_to_services_page()
        self.services_page.open_search_page()
        self.search_page.search(app_name)
        self.search_page.click_element_by_name(app_name)
        self.assertTrue(self.medical_insurance_main_page.is_displayed())

    @login
    def test_04_open_education_pay_success(self):
        """打开教育缴费应用成功"""
        self.main_page.switch_to_services_page()
        self.services_page.select_education_category()
        self.services_page.click_education_pay_image()
        self.assertTrue(self.common_pay_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
