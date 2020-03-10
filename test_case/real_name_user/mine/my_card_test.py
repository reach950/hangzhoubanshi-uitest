#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试我的卡包"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestMyCard(BaseCase):
    """我的-我的证照-证照列表"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_need_face_verification_to_open_identity_card_page(self):
        """已实名，打开居民身份证需要进行人脸识别"""
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_card()
        self.my_card_page.wait_to_display()
        self.my_card_page.click_identity_card()
        self.assertTrue(self.face_verification_page.is_displayed())


if __name__ == '__main__':
    unittest.main()
