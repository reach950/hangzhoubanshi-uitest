#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试投诉建议"""

__author__ = 'kejie'

import unittest
import time
from test_case.base_case import BaseCase
from common_test_step import login


class TestComplaintSuggestion(BaseCase):
    """我的-投诉建议-投诉建议"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_add_complaint(self):
        """添加投诉建议"""
        text = '自动化测试投诉建议，请忽略_{}'.format(int(time.time()))
        self.main_page.switch_to_mine_page()
        self.mine_page.open_complaint_suggestion()
        self.complaint_suggestion_page.open_add_complaint_suggestion_page()
        complaint_type = self.add_complaint_suggestion_page.add_complaint_suggestion(text)
        # 返回到投诉建议页面
        self.assertTrue(self.complaint_suggestion_page.is_displayed())
        # 查看详情
        self.complaint_suggestion_page.click_element_by_name(complaint_type)
        # 验证投诉建议详情页面信息
        self.assertTrue(self.complaint_suggestion_detail_page.is_displayed())
        self.assertTrue(self.complaint_suggestion_detail_page.check_element_by_name(text))
        self.assertTrue(self.complaint_suggestion_detail_page.check_element_by_name(complaint_type))


if __name__ == '__main__':
    unittest.main()
