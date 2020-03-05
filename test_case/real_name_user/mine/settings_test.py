#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试设置"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestClearCache(BaseCase):
    """我的-设置-清理缓存"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_clear_cache(self):
        """清理缓存，空间显示为0"""
        self.main_page.switch_to_mine_page()
        self.mine_page.click_settings()

        cache_size = self.settings_page.get_cache_size()
        self.settings_page.clear_cache()
        self.assertTrue(self.settings_page.is_cache_cleared(cache_size))


if __name__ == '__main__':
    unittest.main()
