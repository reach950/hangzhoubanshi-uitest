#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试高频事项"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestFrequentAffairs(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # 测试打开智能客服页面
    def test_open_ai_customer_service_page(self):
        self.index_page.open_ai_customer_service_page()
        self.assertTrue(self.ai_customer_service_page.is_displayed(),
                        '智能客服页面没有打开')

    # 测试打开个人办事指南详情
    def test_open_personal_guide_detail(self):
        self.index_page.open_handle_affairs_guide_page()
        self.handle_affairs_guide_select_page.open_handle_personal_affairs_page()
        first_affair_name = self.handle_personal_affairs_guide_page.get_first_affair_name()
        self.handle_personal_affairs_guide_page.open_first_affair_guide()
        self.assertTrue(self.guide_detail_page.check_guide_detail_display_by_name(first_affair_name),
                        '<{}>指南详情打开失败'.format(first_affair_name))


if __name__ == '__main__':
    unittest.main()
