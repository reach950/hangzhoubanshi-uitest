#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试搜索"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.login import login


class TestSearchByText(BaseCase):
    """首页-搜索-文字搜索"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login(True)
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
        self.index_page.open_search_page()
        hot_search_words = ['公积金', '社保', '资格证书', '护照', '交通违法', '驾驶员记分', '摇号']
        test_hot_search_words = self.search_page.get_all_hot_search_words()
        self.assertEqual(set(hot_search_words), set(test_hot_search_words))

    def test_04_search_by_text_success(self):
        """搜索结果包含办事事项、服务、预约、办事指南、资讯5类"""
        search_text = '社保'
        # 搜索结果中的办事事项
        item_name = '基本医疗保险关系转移(医保关系转移)'
        # 搜索结果中的服务（页面中只显示两个按钮，用服务代替）
        service_name = '服务'
        # 搜索结果中的预约
        reserve_name = '社会保险职工参保登记'
        # 搜索结果中的办事指南
        guide_name = '人力社保工作监督检查'
        # 搜索结果中的资讯
        news_name = '资讯'
        self.index_page.open_search_page()
        self.search_page.search(search_text)
        self.assertTrue(self.search_page.check_element_by_name(item_name),
                        '没有显示搜索{}的办事事项结果'.format(search_text))
        self.assertTrue(self.search_page.check_element_by_name(service_name),
                        '没有显示搜索{}的服务结果'.format(search_text))
        self.assertTrue(self.search_page.check_element_by_name(reserve_name),
                        '没有显示搜索{}的预约结果'.format(search_text))
        self.assertTrue(self.search_page.check_element_by_name(guide_name),
                        '没有显示搜索{}的办事指南结果'.format(search_text))
        self.search_page.scroll_to_last_search_result()
        self.assertTrue(self.search_page.check_element_by_name(news_name),
                        '没有显示搜索{}的资讯结果'.format(search_text))

    def test_05_search_by_text_has_no_result(self):
        """搜索没有结果，显示6条热门事项"""
        search_text = 'no_result_text'
        no_result_hot_items = ['驾驶证遗失补证', '驾驶证超龄换证', '驾驶证期满换证',
                               '驾驶证损毁换证', '客运出租汽车驾驶员从业资格认定', '驾照扣分查询']
        self.index_page.open_search_page()
        self.search_page.search(search_text)
        self.assertTrue(self.search_page.is_no_result_page_display())
        test_no_result_hot_items = self.search_page.get_no_result_hot_items()
        self.assertEqual(set(no_result_hot_items), set(test_no_result_hot_items))


if __name__ == '__main__':
    unittest.main()
