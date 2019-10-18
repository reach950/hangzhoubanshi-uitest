#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试杭州发布"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestHzNews(BaseCase):
    """首页-杭州发布-发布新闻"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_click_more_button_open_news_page(self):
        """点击更多按钮打开资讯页面"""
        self.index_page.scroll_to_news()
        self.index_page.click_hz_news_more_button()
        self.assertTrue(self.news_page.is_displayed(), '打开资讯页面失败')

    def test_02_open_news_detail(self):
        """点击打开资讯详情"""
        self.index_page.scroll_to_news()
        first_news_title = self.index_page.get_first_news_title()
        first_news_source = self.index_page.get_first_news_source()
        self.index_page.open_first_news_detail()
        self.assertIn(first_news_title, self.news_detail_page.get_news_title(first_news_source))


if __name__ == '__main__':
    unittest.main()
