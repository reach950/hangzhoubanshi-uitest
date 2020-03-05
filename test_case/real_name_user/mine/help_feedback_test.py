#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试求助反馈"""

__author__ = 'kejie'

import unittest
from datetime import datetime
from test_case.base_case import BaseCase


class TestFrequentlyQuestion(BaseCase):
    """我的-求助反馈-常见问题"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_hide_answer(self):
        """打开折叠问题答案"""
        question_text = '忘记密码怎么办？'
        reply_text = '如密码遗忘，可通过登陆界面的“忘记密码”进行密码重置。'
        self.main_page.switch_to_mine_page()
        self.mine_page.click_help_feedback()
        self.help_feedback_page.click_problem_to_seek_help()
        self.problem_to_seek_help_page.wait_to_display()
        # 答案折叠，没有显示
        self.assertTrue(self.problem_to_seek_help_page.is_reply_disappeared(reply_text))
        self.problem_to_seek_help_page.click_question(question_text)
        # 打开折叠答案，正常显示
        self.assertTrue(self.problem_to_seek_help_page.is_reply_displayed(reply_text))
        self.problem_to_seek_help_page.click_question(question_text)
        # 答案折叠，没有显示
        self.assertTrue(self.problem_to_seek_help_page.is_reply_disappeared(reply_text))


class TestFeedback(BaseCase):
    """我的-求助反馈-意见反馈"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_publish_feedback(self):
        """发布意见反馈"""
        feedback_text = '自动化测试意见反馈，请忽略_{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        self.main_page.switch_to_mine_page()
        self.mine_page.click_help_feedback()
        self.help_feedback_page.click_feedback()

        feedback_type = self.feedback_page.select_random_feedback_type()
        # 未输入文本，提交按钮不可用
        self.assertFalse(self.feedback_page.is_submit_button_enabled())
        self.feedback_page.input_text(feedback_text)
        self.feedback_page.scroll_to_footer()
        self.feedback_page.click_submit_button()

        self.help_feedback_page.click_my_suggestion()
        self.my_suggestion_page.click_first_suggestion_view_detail()
        # 进入建议详情
        self.assertTrue(self.suggestion_detail_page.is_displayed())
        # 新的意见反馈
        self.assertTrue(self.suggestion_detail_page.is_handle_status_displayed('已受理'))
        self.assertTrue(self.suggestion_detail_page.is_suggestion_type_displayed(feedback_type))
        self.assertTrue(self.suggestion_detail_page.is_suggestion_content_displayed(feedback_text))


if __name__ == '__main__':
    unittest.main()
