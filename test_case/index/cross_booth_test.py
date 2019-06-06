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
    def test_handle_page_test(self):
        self.index_page.open_handle_page()
        self.assertTrue(self.handle_page.is_displayed(), '我要办理页面无法打开')
        self.handle_page.search(self.search_text)
        self.assertTrue(self.handle_page.check_element_by_name(self.handle_search_result), '搜索结果错误')
        self.assertFalse(self.handle_page.check_element_by_name(self.query_search_result, 3), '搜索结果错误')
        self.assertFalse(self.handle_page.check_element_by_name(self.pay_search_result, 3), '搜索结果错误')

    # 测试我要查询页面
    def test_query_page_test(self):
        self.index_page.open_query_page()
        self.assertTrue(self.query_page.is_displayed(), '我要办理页面无法打开')
        self.query_page.search(self.search_text)
        self.assertTrue(self.query_page.check_element_by_name(self.query_search_result), '搜索结果错误')
        self.assertFalse(self.query_page.check_element_by_name(self.handle_search_result, 3), '搜索结果错误')
        self.assertFalse(self.query_page.check_element_by_name(self.pay_search_result, 3), '搜索结果错误')

    # 测试我要查询页面
    def test_pay_page_test(self):
        self.index_page.open_pay_page()
        self.assertTrue(self.pay_page.is_displayed(), '我要办理页面无法打开')
        self.pay_page.search(self.search_text)
        self.assertTrue(self.pay_page.check_element_by_name(self.pay_search_result), '搜索结果错误')
        self.assertFalse(self.pay_page.check_element_by_name(self.handle_search_result, 3), '搜索结果错误')
        self.assertFalse(self.pay_page.check_element_by_name(self.query_search_result, 3), '搜索结果错误')


if __name__ == '__main__':
    unittest.main()
