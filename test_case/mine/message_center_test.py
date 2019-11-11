#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试消息中心"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login


class TestMessageType(BaseCase):
    """我的-消息中心-消息类型"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_handle_item_detail_page(self):
        """点击办件消息，跳转到对应的办件详情页面"""
        self.assertTrue(True)

    @login
    def test_02_open_reserve_detail_page(self):
        """点击预约消息，跳转到对应的预约详情页面"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
