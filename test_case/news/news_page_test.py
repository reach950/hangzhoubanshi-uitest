#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试资讯页面"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestNewsPage(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # 测试发布日期排序
    def test_publish_date_sort(self):
        self.index_page.switch_to_news_page()
        publish_dates = self.news_page.get_all_publish_date()
        for i in range(0, len(publish_dates) - 1):
            self.assertTrue(publish_dates[i] >= publish_dates[i + 1])

    # 测试资讯详情是否打开
    def test_open_news_detail(self):
        self.index_page.switch_to_news_page()
        self.news_page.switch_to_hzfb_tab()
        first_news_title = self.news_page.get_first_news_title()
        self.news_page.open_first_news()
        self.assertEqual(first_news_title, self.news_detail_page.get_news_title(), '资讯详情打开失败')


if __name__ == '__main__':
    unittest.main()
