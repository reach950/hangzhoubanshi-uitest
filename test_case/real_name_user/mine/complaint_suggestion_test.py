#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试投诉建议"""

__author__ = 'kejie'

import unittest
from datetime import datetime
from test_case.base_case import BaseCase


class TestComplaintSuggestion(BaseCase):
    """我的-投诉建议-投诉建议"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_add_complaint(self):
        """添加投诉建议"""
        complaint_text = '自动化测试投诉建议，请忽略_{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        self.main_page.switch_to_mine_page()
        self.mine_page.click_complaint_suggestion()
        self.complaint_suggestion_page.click_add_department_complaint_suggestion()
        complaint_type = self.add_complaint_suggestion_page.add_complaint_suggestion(complaint_text)
        # 返回到投诉建议页面
        self.assertTrue(self.complaint_suggestion_page.is_displayed())
        # 查看详情
        self.complaint_suggestion_page.click_first_complaint_by_complaint_type(complaint_type)
        # 验证投诉建议详情页面信息
        self.assertTrue(self.complaint_suggestion_detail_page.is_displayed())
        self.assertTrue(self.complaint_suggestion_detail_page.is_contain_complaint_content(complaint_text))


if __name__ == '__main__':
    unittest.main()
