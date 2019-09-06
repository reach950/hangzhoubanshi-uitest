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
    def test_open_ai_customer_service_page(self):
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
    def test_open_personal_guide_detail(self):
        """打开个人办事指南详情"""
        self.index_page.open_handle_items_guide_page()
        self.handle_items_guide_select_page.open_handle_personal_items_page()
        first_item_name = self.handle_personal_items_guide_page.get_first_item_name()
        self.handle_personal_items_guide_page.open_first_item_guide()
        self.assertTrue(self.guide_detail_page.check_guide_detail_display_by_name(first_item_name),
                        '<{}>指南详情打开失败'.format(first_item_name))


if __name__ == '__main__':
    unittest.main()
