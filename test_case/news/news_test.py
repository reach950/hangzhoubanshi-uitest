#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试新闻资讯"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestNews(BaseCase):
    """生活-新闻资讯-新闻资讯"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_publish_date_sort(self):
        """新闻资讯按发布时间降序排列"""
        self.index_page.switch_to_news_page()
        publish_dates = self.news_page.get_all_publish_date()
        for i in range(0, len(publish_dates) - 1):
            self.assertTrue(publish_dates[i] >= publish_dates[i + 1])

    def test_open_news_detail(self):
        """打开杭州发布资讯详情"""
        self.index_page.switch_to_news_page()
        self.news_page.switch_to_hzfb_tab()
        first_news_title = self.news_page.get_first_news_title()
        self.news_page.open_first_news()
        self.assertEqual(first_news_title, self.news_detail_page.get_hzfb_news_title(), '资讯详情打开失败')


if __name__ == '__main__':
    unittest.main()
