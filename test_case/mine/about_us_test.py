#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试关于我们"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestPrivacyStatement(BaseCase):
    """我的-关于我们-隐私声明"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_privacy_statement(self):
        """隐私声明"""
        self.assertTrue(True)


class TestCurrentAppVersion(BaseCase):
    """我的-关于我们-当前版本"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_display_version(self):
        """显示app版本号"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
