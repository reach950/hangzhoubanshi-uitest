#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试投诉建议"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestComplaint(BaseCase):
    """我的-投诉建议-投诉建议"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_create_complaint(self):
        """添加投诉建议"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
