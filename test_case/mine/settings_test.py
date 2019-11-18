#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试设置"""

__author__ = 'kejie'

import unittest
import time
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestClearCache(BaseCase):
    """我的-设置-清理缓存"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_clear_cache(self):
        """清理缓存，空间显示为0"""
        self.index_page.switch_to_mine_page()
        self.mine_page.open_settings_page()
        self.settings_page.clear_cache()
        time.sleep(3)
        self.assertEqual(self.settings_page.get_cache_size(), '0.00M')


if __name__ == '__main__':
    unittest.main()
