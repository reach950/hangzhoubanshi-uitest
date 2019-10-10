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

    @login(True)
    def test_02_open_ai_customer_service_page_by_small_icon(self):
        """点击客服小图标，打开智能客服页面成功"""
        self.index_page.open_ai_customer_service_page_by_small_icon()
        self.assertTrue(self.ai_customer_service_page.is_displayed(),
                        '智能客服页面没有打开')

    @login(True)
    def test_03_get_reply_from_default_question(self):
        """点击默认问题，获取正确回复"""
        default_question = '如何查找办理业务所需要的材料'
        default_question_reply = '可以在主页搜索，或者点击办事指南查找办事材料'
        self.index_page.open_ai_customer_service_page()
        self.ai_customer_service_page.click_default_question(default_question)
        self.assertTrue(self.ai_customer_service_page.check_element_by_name(default_question_reply))

    @login(True)
    def test_04_get_reply_from_search_by_text(self):
        """通过文本搜索，获取正确回复"""
        search_text = '社保咨询热线是多少'
        search_text_reply = '社保咨询服务热线：12333。'
        self.index_page.open_ai_customer_service_page()
        self.ai_customer_service_page.search(search_text)
        self.assertTrue(self.ai_customer_service_page.check_element_by_name(search_text_reply))


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
