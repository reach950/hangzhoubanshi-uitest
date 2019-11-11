#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试求助反馈"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestFrequentlyQuestion(BaseCase):
    """我的-求助反馈-常见问题"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_hide_answer(self):
        """打开折叠问题答案"""
        self.assertTrue(True)


class TestFeedback(BaseCase):
    """我的-求助反馈-意见反馈"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_publish_feedback(self):
        """发布意见反馈"""
        self.assertTrue(True)


class TestMySuggestion(BaseCase):
    """我的-求助反馈-我的建议"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_new_feedback_detail(self):
        """新的意见反馈详情"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
