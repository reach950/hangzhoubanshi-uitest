#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试求助反馈"""

__author__ = 'kejie'

import unittest
import time
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
        question_text = '忘记密码怎么办？'
        answer_text = '如密码遗忘，可通过登陆界面的“忘记密码”进行密码重置。'
        self.index_page.switch_to_mine_page()
        self.mine_page.open_help_feedback()
        self.help_feedback_page.open_problem_to_seek_help()
        # 答案折叠，没有显示
        self.assertFalse(self.problem_to_seek_help_page.check_element_by_name(answer_text))
        self.problem_to_seek_help_page.click_element_by_name(question_text)
        # 打开折叠答案，正常显示
        self.assertTrue(self.problem_to_seek_help_page.check_element_by_name(answer_text))


class TestFeedback(BaseCase):
    """我的-求助反馈-意见反馈"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_publish_feedback(self):
        """发布意见反馈"""
        text = '自动化测试意见反馈，请忽略_{}'.format(int(time.time()))
        self.index_page.switch_to_mine_page()
        self.mine_page.open_help_feedback()
        self.help_feedback_page.open_feedback()

        problem_type = self.feedback_page.select_random_problem_type()
        # 未输入文本，提交按钮不可用
        self.assertFalse(self.feedback_page.is_submit_button_enabled())
        self.feedback_page.input_text(text)
        self.feedback_page.scroll_to_footer()
        self.feedback_page.click_submit_button()

        self.help_feedback_page.open_my_suggestion()
        self.my_suggestion_page.open_first_suggestion_detail()
        # 进入建议详情
        self.assertTrue(self.suggestion_detail_page.is_displayed())
        # 新的意见反馈
        self.assertTrue(self.suggestion_detail_page.check_element_by_name('已受理'))
        self.assertTrue(self.suggestion_detail_page.check_element_by_name(problem_type))
        self.assertTrue(self.suggestion_detail_page.check_element_by_name(text))


if __name__ == '__main__':
    unittest.main()
