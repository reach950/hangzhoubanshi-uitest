#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试高频事项"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestAICustomerService(BaseCase):
    """首页-高频事项-智能客服"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_ai_customer_service_page(self):
        """打开智能客服页面成功"""
        self.main_page.click_ai_service()
        self.assertTrue(self.ai_customer_service_page.is_displayed(),
                        '智能客服页面没有打开')

    def test_02_open_ai_customer_service_page_by_small_icon(self):
        """点击客服小图标，打开智能客服页面成功"""
        self.main_page.click_ai_service_small_icon()
        self.assertTrue(self.ai_customer_service_page.is_displayed(),
                        '智能客服页面没有打开')

    def test_03_get_reply_from_default_question(self):
        """点击默认问题，获取正确回复"""
        default_question = '年长的父母不愿意戴口罩怎么办'
        default_question_reply = '从官方公布的疫情看'
        self.main_page.click_ai_service()
        self.ai_customer_service_page.click_default_question(default_question)
        self.assertTrue(self.ai_customer_service_page.is_reply_display(default_question_reply, full=False))

    def test_04_get_reply_from_search_by_text(self):
        """通过文本搜索，获取正确回复"""
        search_text = '社保咨询热线是多少'
        search_text_reply = '社保咨询服务热线：12333。'
        self.main_page.click_ai_service()
        self.ai_customer_service_page.search(search_text)
        self.assertTrue(self.ai_customer_service_page.check_element_by_name(search_text_reply))


class TestItemsGuide(BaseCase):
    """首页-高频事项-办事指南"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_personal_guide_list_success(self):
        """打开个人办事指南列表成功"""
        self.main_page.click_guide()
        self.guide_select_page.click_personal_guide()
        self.assertTrue(self.personal_or_legal_guide_list_page.is_displayed('个人办事'))

    def test_02_open_legal_guide_list_success(self):
        """打开法人办事指南列表成功"""
        self.main_page.click_guide()
        self.guide_select_page.click_legal_guide()
        self.assertTrue(self.personal_or_legal_guide_list_page.is_displayed('法人办事'))

    def test_03_search_guide_success(self):
        """搜索个人办事指南成功"""
        search_text = '公积金'
        self.main_page.click_guide()
        self.guide_select_page.click_personal_guide()
        self.personal_or_legal_guide_list_page.search(search_text)
        first_item_guide_name = self.personal_or_legal_guide_list_page.get_first_guide_name()
        self.assertIn(search_text, first_item_guide_name)

    def test_04_filter_guide_success(self):
        """分类tab筛选个人办事指南成功"""
        self.main_page.click_guide()
        self.guide_select_page.click_personal_guide()
        before_filter_first_item_guide_name = self.personal_or_legal_guide_list_page.get_first_guide_name()
        self.personal_or_legal_guide_list_page.change_target_to_children_and_adolescents()
        after_filter_first_item_guide_name = self.personal_or_legal_guide_list_page.get_first_guide_name()
        # 筛选后第一条指南不相同
        self.assertNotEqual(before_filter_first_item_guide_name, after_filter_first_item_guide_name)

    def test_05_personal_guide_detail_display_correct(self):
        """个人办事指南详情内容显示正常"""
        self.main_page.click_guide()
        self.guide_select_page.click_personal_guide()
        first_item_name = self.personal_or_legal_guide_list_page.get_first_guide_name()
        self.personal_or_legal_guide_list_page.click_first_guide()
        self.assertTrue(self.guide_detail_page.is_displayed(), '<{}>指南详情打开失败'.format(first_item_name))
        self.assertTrue(self.guide_detail_page.check_element_by_name(first_item_name),
                        '<{}>指南详情打开失败'.format(first_item_name))


if __name__ == '__main__':
    unittest.main()
