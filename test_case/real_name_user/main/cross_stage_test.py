#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试十字展台"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step import login
from common_test_step import reserve

search_text = '联通'
# 我要办理搜索联通包含的事项
handle_search_result = '联通移动电话产品变更(电话产品变更)'
# 我要查询搜索联通包含的事项
query_search_result = '联通移动电话实时话费(实时话费查询)'
# 我要缴费搜索联通包含的事项
pay_search_result = '联通移动电话缴费(电话缴费)'


@unittest.skip
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
        self.main_page.scroll_to_cross_stage()
        self.main_page.open_reserve_page()
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
