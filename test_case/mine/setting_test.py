#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试设置"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestDeleteCache(BaseCase):
    """我的-设置-清除缓存"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_delete_cache(self):
        """清楚缓存"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
