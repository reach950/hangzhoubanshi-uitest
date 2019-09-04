#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试杭州资讯"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestHzNews(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # 测试点击更多按钮打开资讯页面
    def test_click_more_button_open_news_page(self):
        self.index_page.click_hz_news_more_button()
        self.assertTrue(self.news_page.is_displayed(), '打开资讯页面失败')

    # 测试打开资讯详情
    def test_open_news_detail(self):
        first_news_title = self.index_page.get_first_news_title()
        self.index_page.open_first_news_detail()
        self.assertIn(first_news_title, self.news_detail_page.get_hzfb_news_title())


if __name__ == '__main__':
    unittest.main()
