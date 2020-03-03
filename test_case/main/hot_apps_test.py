#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试热门应用"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestAllApps(BaseCase):
    """首页-热门应用-全部"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_all_apps_page_success(self):
        """点击全部，跳转到全部应用"""
        self.main_page.click_more_apps()
        self.assertTrue(self.all_apps_page.is_displayed())

    def test_02_search_success(self):
        """搜索"""
        search_text = '联通'
        # 我要办理搜索联通包含的事项
        handle_search_result = '联通移动电话产品变更(电话产品变更)'
        # 我要查询搜索联通包含的事项
        query_search_result = '联通移动电话实时话费(实时话费查询)'
        # 我要缴费搜索联通包含的事项
        pay_search_result = '联通移动电话缴费(电话缴费)'
        self.main_page.click_more_apps()
        self.all_apps_page.search(search_text)
        self.assertTrue(self.all_apps_page.is_search_result_contain_handle_item(handle_search_result))
        self.assertTrue(self.all_apps_page.is_search_result_contain_query_item(query_search_result))
        self.assertTrue(self.all_apps_page.is_search_result_contain_pay_item(pay_search_result))

    def test_03_open_ai_service_success(self):
        """智能客服"""
        self.main_page.click_more_apps()
        self.all_apps_page.click_ai_service_icon()
        self.assertTrue(self.ai_customer_service_page.is_displayed())

    def test_04_open_handle_item_success(self):
        """打开办理类事项"""
        item_name = '出具社会保险信息证明'
        self.main_page.click_more_apps()
        self.all_apps_page.switch_to_handle_tab()
        self.all_apps_page.click_element_by_name(item_name)
        self.assertTrue(self.provide_social_insurance_certificate_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
