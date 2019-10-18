#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试十字展台"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login
from test_case.common_test_step import reserve

search_text = '联通'
# 我要办理搜索联通包含的事项
handle_search_result = '联通移动电话产品变更(电话产品变更)'
# 我要查询搜索联通包含的事项
query_search_result = '联通移动电话实时话费(实时话费查询)'
# 我要缴费搜索联通包含的事项
pay_search_result = '联通移动电话缴费(电话缴费)'


class TestHandleItems(BaseCase):
    """首页-十字展台-我要办理"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_ai_customer_service_page_success(self):
        """点击客服图标，打开智能客服页面成功"""
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_handle_page()
        self.assertTrue(self.handle_page.is_displayed(), '我要办理页面无法打开')
        self.handle_page.open_customer_service_page()
        self.assertTrue(self.ai_customer_service_page.is_displayed())

    @login
    def test_02_search_handle_items(self):
        """我要办理页面只能搜索出办理的事项"""
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_handle_page()
        self.handle_page.search(search_text)
        self.assertTrue(self.handle_page.check_element_by_name(handle_search_result), '搜索结果错误')
        self.assertFalse(self.handle_page.check_element_by_name(query_search_result, 3), '搜索结果错误')
        self.assertFalse(self.handle_page.check_element_by_name(pay_search_result, 3), '搜索结果错误')


class TestPayItems(BaseCase):
    """首页-十字展台-我要缴费"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_ai_customer_service_page_success(self):
        """点击客服图标，打开智能客服页面成功"""
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_pay_page()
        self.assertTrue(self.pay_page.is_displayed(), '我要缴费页面无法打开')
        self.pay_page.open_customer_service_page()
        self.assertTrue(self.ai_customer_service_page.is_displayed())

    @login
    def test_02_search_pay_items(self):
        """我要缴费页面只能搜索出缴费的事项"""
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_pay_page()
        self.pay_page.search(search_text)
        self.assertTrue(self.pay_page.check_element_by_name(pay_search_result), '搜索结果错误')
        self.assertFalse(self.pay_page.check_element_by_name(handle_search_result, 3), '搜索结果错误')
        self.assertFalse(self.pay_page.check_element_by_name(query_search_result, 3), '搜索结果错误')


class TestQueryItems(BaseCase):
    """首页-十字展台-我要查询"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_ai_customer_service_page_success(self):
        """点击客服图标，打开智能客服页面成功"""
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_query_page()
        self.assertTrue(self.query_page.is_displayed(), '我要查询页面无法打开')
        self.query_page.open_customer_service_page()
        self.assertTrue(self.ai_customer_service_page.is_displayed())

    @login
    def test_02_search_query_items(self):
        """我要查询页面只能搜索出查询的事项"""
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_query_page()
        self.query_page.search(search_text)
        self.assertTrue(self.query_page.check_element_by_name(query_search_result), '搜索结果错误')
        self.assertFalse(self.query_page.check_element_by_name(handle_search_result, 3), '搜索结果错误')
        self.assertFalse(self.query_page.check_element_by_name(pay_search_result, 3), '搜索结果错误')


class TestReserveItems(BaseCase):
    """首页-十字展台-我要预约"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_reserve_success_to_open_activate_page(self):
        """预约成功，跳转到激活预约页面"""
        reserve_info = reserve.get_reserve_item(self.driver)
        self.index_page.scroll_to_cross_stage()
        self.index_page.open_reserve_page()
        self.reserve_page.open_query_reserve_info_page()
        # 检查预约记录里的第一条预约状态
        self.assertEqual(self.reserve_record_page.get_first_reserve_record_state(), '预约成功')
        self.reserve_record_page.open_first_reserve_detail_page()
        self.assertTrue(self.activate_reserve_page.is_displayed(), '激活预约页面打开失败')
        # 检查激活预约页面的办事时间
        self.assertEqual(self.activate_reserve_page.get_reserve_time(), reserve_info['办事时间'])
        # 检查激活预约页面的预约事项
        self.assertEqual(self.activate_reserve_page.get_reserve_item_name(), reserve_info['预约事项'])
        self.activate_reserve_page.open_how_to_scan_code_page()
        self.assertTrue(self.how_to_scan_code_page.is_displayed(), '如何扫码页面打开失败')

    @login
    def test_02_cancel_reserve(self):
        """取消预约"""
        reserve.get_reserve_item(self.driver)
        reserve.cancel_reserve(self.driver)
        # 检查预约记录里的第一条预约状态
        self.assertEqual(self.reserve_record_page.get_first_reserve_record_state(), '已取消')


if __name__ == '__main__':
    unittest.main()
