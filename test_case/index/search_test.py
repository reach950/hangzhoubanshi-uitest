#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试搜索"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestSearch(BaseCase):

    def setUp(self):
        super().setUp()
        self.search_text = '社保'
        # 搜索结果中的第一个办事事项
        self.first_affair_name = '基本医疗保险关系转移(医保关系转移)'

    def tearDown(self):
        super().tearDown()

    # 测试文字搜索
    def test_search_by_text(self):
        self.index_page.open_search_page()
        self.search_page.search(self.search_text)
        self.assertTrue(self.search_page.check_element_by_name(self.first_affair_name),
                        '没有显示搜索{}的结果'.format(self.search_text))


if __name__ == '__main__':
    unittest.main()
