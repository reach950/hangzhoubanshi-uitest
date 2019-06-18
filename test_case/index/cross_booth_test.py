#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试十字展台"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestCrossBooth(BaseCase):

    def setUp(self):
        super().setUp()
        self.search_text = '联通'
        # 我要办理搜索联通包含的事项
        self.handle_search_result = '联通移动电话产品变更(电话产品变更)'
        # 我要查询搜索联通包含的事项
        self.query_search_result = '联通移动电话实时话费(实时话费查询)'
        # 我要缴费搜索联通包含的事项
        self.pay_search_result = '联通移动电话缴费(电话缴费)'

    def tearDown(self):
        super().tearDown()

    # 测试我要办理页面
    def test_handle_page(self):
        self.index_page.open_handle_page()
        self.assertTrue(self.handle_page.is_displayed(), '我要办理页面无法打开')
        self.handle_page.search(self.search_text)
        self.assertTrue(self.handle_page.check_element_by_name(self.handle_search_result), '搜索结果错误')
        self.assertFalse(self.handle_page.check_element_by_name(self.query_search_result, 3), '搜索结果错误')
        self.assertFalse(self.handle_page.check_element_by_name(self.pay_search_result, 3), '搜索结果错误')

    # 测试我要查询页面
    def test_query_page(self):
        self.index_page.open_query_page()
        self.assertTrue(self.query_page.is_displayed(), '我要办理页面无法打开')
        self.query_page.search(self.search_text)
        self.assertTrue(self.query_page.check_element_by_name(self.query_search_result), '搜索结果错误')
        self.assertFalse(self.query_page.check_element_by_name(self.handle_search_result, 3), '搜索结果错误')
        self.assertFalse(self.query_page.check_element_by_name(self.pay_search_result, 3), '搜索结果错误')

    # 测试我要缴费页面
    def test_pay_page(self):
        self.index_page.open_pay_page()
        self.assertTrue(self.pay_page.is_displayed(), '我要办理页面无法打开')
        self.pay_page.search(self.search_text)
        self.assertTrue(self.pay_page.check_element_by_name(self.pay_search_result), '搜索结果错误')
        self.assertFalse(self.pay_page.check_element_by_name(self.handle_search_result, 3), '搜索结果错误')
        self.assertFalse(self.pay_page.check_element_by_name(self.query_search_result, 3), '搜索结果错误')

    # 测试预约
    def test_reserve(self):
        self.index_page.open_reserve_page()
        self.reserve_page.open_hangzhou_civic_center_page()
        self.hangzhou_civic_center_page.open_housing_provident_funds_page()
        self.housing_provident_funds_page.click_personal_housing_provident_funds_free()
        self.reserve_time_page.click_first_reserve_time()
        reserve_info = self.reserve_info_confirm_page.get_reserve_info()
        self.reserve_info_confirm_page.click_confirm_reserve_info_button()
        self.reserve_success_page.click_back_to_index_button()

        self.reserve_page.open_query_reserve_info_page()
        # 检查预约记录里的第一条预约状态
        self.assertEqual(self.reserve_record_page.get_first_reserve_record_state(), '预约成功')
        self.reserve_record_page.open_first_reserve_detail_page()
        self.assertTrue(self.activate_reserve_page.is_displayed(), '激活预约页面打开失败')
        # 检查激活预约页面的办事时间
        self.assertEqual(self.activate_reserve_page.get_reserve_time(), reserve_info['办事时间'])
        # 检查激活预约页面的预约事项
        self.assertEqual(self.activate_reserve_page.get_reserve_affair_name(), reserve_info['预约事项'])
        self.activate_reserve_page.cancel_reserve()
        # 检查预约记录里的第一条预约状态
        self.assertEqual(self.reserve_record_page.get_first_reserve_record_state(), '已取消')
        self.reserve_record_page.open_first_reserve_detail_page()
        self.assertTrue(self.reserve_detail_page.is_displayed(), '预约详情页面打开失败')
        reserve_info_history = self.reserve_detail_page.get_reserve_info()
        for i in reserve_info:
            if i == '办事大厅':
                # 预约历史记录里办事大厅多了个具体位置
                self.assertIn(reserve_info[i], reserve_info_history[i])
            else:
                self.assertEqual(reserve_info[i], reserve_info_history[i])


if __name__ == '__main__':
    unittest.main()
