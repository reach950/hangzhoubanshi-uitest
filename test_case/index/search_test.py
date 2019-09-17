#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试搜索"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestSearchByText(BaseCase):
    """首页-搜索-文字搜索"""

    def setUp(self):
        super().setUp()
        self.search_text = '社保'
        # 搜索结果中的第一个办事事项
        self.first_affair_name = '基本医疗保险关系转移(医保关系转移)'

    def tearDown(self):
        super().tearDown()

    def test_01_open_ai_customer_service_page_success(self):
        """点击客服按钮打开智能客服成功"""
        self.index_page.open_search_page()
        self.search_page.click_customer_service_button()
        self.assertTrue(self.ai_customer_service_page.is_displayed())

    def test_02_cancle_search_return_index_page(self):
        """取消搜索，返回主页"""
        self.index_page.open_search_page()
        self.search_page.cancel_search()
        self.assertTrue(self.index_page.is_displayed())

    def test_03_hot_search_words(self):
        """测试热门搜索词"""
        hot_search_words = ['公积金', '社保', '资格证书', '护照', '交通违法', '驾驶员记分', '摇号']
        self.index_page.open_search_page()
        test_hot_search_words = self.search_page.get_all_hot_search_words()
        self.assertEqual(set(hot_search_words), set(test_hot_search_words))

    def test_search_by_text_success(self):
        """输入关键字搜索结果成功"""
        self.index_page.open_search_page()
        self.search_page.search(self.search_text)
        self.assertTrue(self.search_page.check_element_by_name(self.first_affair_name),
                        '没有显示搜索{}的结果'.format(self.search_text))


if __name__ == '__main__':
    unittest.main()
