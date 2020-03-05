#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试主题模版应用"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestThemeApps(BaseCase):
    """服务-主题模版应用-主题应用"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_car_quota_success(self):
        """打开小客车指标应用成功"""
        self.main_page.switch_to_services_page()
        self.services_page.select_traffic_category()
        self.services_page.click_car_quota()
        self.assertTrue(self.car_quota_main_page.is_displayed())

    def test_02_open_mobile_population_registration_success(self):
        """打开流动人口登记应用成功"""
        self.main_page.switch_to_services_page()
        self.services_page.select_residence_registration_category()
        self.services_page.click_mobile_population_reside_registration()
        self.assertTrue(self.mobile_population_reside_registration_page.is_displayed())

    def test_03_open_medical_insurance_success(self):
        """打开养老保险应用成功"""
        app_name = '养老保险'
        self.main_page.switch_to_services_page()
        self.services_page.click_search_field()
        self.search_page.search(app_name)
        self.search_page.click_endowment_insurance()
        self.assertTrue(self.endowment_insurance_page.is_displayed())

    def test_04_open_education_pay_success(self):
        """打开教育缴费应用成功"""
        self.main_page.switch_to_services_page()
        self.services_page.select_education_category()
        self.services_page.click_education_pay()
        self.assertTrue(self.common_pay_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
