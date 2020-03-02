#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试地区展台"""

__author__ = 'kejie'

import random
import unittest
from test_case.base_case import BaseCase


class TestDistrictServices(BaseCase):
    """服务-地区展台-区县服务"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_hot_app_only_in_xiacheng_district(self):
        """热门应用只有下城区有，其他区没有"""
        districts = ['市本级', '上城区', '下城区', '江干区', '拱墅区', '西湖区', '滨江区', '余杭区', '萧山区', '临安区',
                     '富阳区', '建德市', '桐庐县', '淳安县', '经济技术开发区', '西湖风景名胜区', '大江东产业集聚区']
        self.main_page.scroll_to_news()
        self.main_page.scroll_to_district_service()
        self.main_page.click_district_service()
        self.district_services_main_page.click_district_select_button()
        self.district_select_page.select_district_by_name(districts[2])
        # 下城区显示热门应用
        self.assertTrue(self.district_services_main_page.is_hot_app_display())
        self.district_services_main_page.click_district_select_button()
        while True:
            random_district = random.choice(districts)
            if random_district != districts[2]:
                self.district_select_page.select_district_by_name(random_district)
                break
        # 非下城区不显示热门应用
        self.district_services_main_page.wait_to_display()
        self.assertTrue(self.district_services_main_page.is_hot_app_disappeared())

    def test_02_hot_departments(self):
        """热门部门默认显示十条，点击更多按钮查看更多部门"""
        self.main_page.scroll_to_news()
        self.main_page.scroll_to_district_service()
        self.main_page.click_district_service()
        self.district_services_main_page.wait_to_display()
        hot_departments = self.district_services_main_page.get_all_hot_departments()
        # 热门部门默认显示十条
        self.assertEqual(len(hot_departments), 10)
        self.district_services_main_page.click_hot_departments_more_button()
        # 点击更多按钮显示全部部门页面
        self.assertTrue(self.all_departments_page.is_displayed())

    def test_03_open_department_item_success(self):
        """打开部门事项成功"""
        self.main_page.scroll_to_news()
        self.main_page.scroll_to_district_service()
        self.main_page.click_district_service()
        self.district_services_main_page.click_transportation_bureau()
        self.transportation_bureau_page.click_car_incremental_quota()
        # 打开小客车增量指标事项成功
        self.assertTrue(self.car_incremental_quota_page.is_display())


if __name__ == '__main__':
    unittest.main()
