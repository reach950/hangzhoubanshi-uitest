#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试高频事项"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.login import login


class TestAICustomerService(BaseCase):
    """首页-高频事项-智能客服"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login(True)
    def test_01_open_ai_customer_service_page(self):
        """打开智能客服页面成功"""
        self.index_page.open_ai_customer_service_page()
        self.assertTrue(self.ai_customer_service_page.is_displayed(),
                        '智能客服页面没有打开')


class TestItemsGuide(BaseCase):
    """首页-高频事项-办事指南"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login(True)
    def test_01_open_personal_guide_list_success(self):
        """打开个人办事指南列表成功"""
        self.index_page.open_handle_items_guide_page()
        self.guide_select_page.open_personal_guide_list_page()
        self.assertTrue(self.personal_or_legal_guide_list_page.is_displayed('个人办事'))

    @login(True)
    def test_02_open_legal_guide_list_success(self):
        """打开法人办事指南列表成功"""
        self.index_page.open_handle_items_guide_page()
        self.guide_select_page.open_legal_guide_list_page()
        self.assertTrue(self.personal_or_legal_guide_list_page.is_displayed('法人办事'))

    @login(True)
    def test_03_search_guide_success(self):
        """搜索个人办事指南成功"""
        search_text = '公积金'
        self.index_page.open_handle_items_guide_page()
        self.guide_select_page.open_personal_guide_list_page()
        self.personal_or_legal_guide_list_page.search(search_text)
        first_item_guide_name = self.personal_or_legal_guide_list_page.get_first_item_guide_name()
        self.assertIn(search_text, first_item_guide_name)

    @login(True)
    def test_04_filter_guide_success(self):
        """分类tab筛选个人办事指南成功"""
        self.index_page.open_handle_items_guide_page()
        self.guide_select_page.open_personal_guide_list_page()
        before_filter_first_item_guide_name = self.personal_or_legal_guide_list_page.get_first_item_guide_name()
        self.personal_or_legal_guide_list_page.change_target_to_children_and_adolescents()
        after_filter_first_item_guide_name = self.personal_or_legal_guide_list_page.get_first_item_guide_name()
        # 筛选后第一条指南不相同
        self.assertNotEqual(before_filter_first_item_guide_name, after_filter_first_item_guide_name)

    @login(True)
    def test_05_personal_guide_detail_display_correct(self):
        """个人办事指南详情内容显示正常"""
        self.index_page.open_handle_items_guide_page()
        self.guide_select_page.open_personal_guide_list_page()
        first_item_name = self.personal_or_legal_guide_list_page.get_first_item_guide_name()
        self.personal_or_legal_guide_list_page.open_first_item_guide()
        self.assertTrue(self.guide_detail_page.check_guide_detail_display_by_name(first_item_name),
                        '<{}>指南详情打开失败'.format(first_item_name))


if __name__ == '__main__':
    unittest.main()
