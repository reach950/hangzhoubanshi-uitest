#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试关于我们"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestPrivacyStatement(BaseCase):
    """我的-关于我们-隐私声明"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_privacy_statement(self):
        """隐私声明"""
        self.main_page.switch_to_mine_page()
        self.mine_page.click_about_us()
        self.about_us_page.click_term_of_service()
        self.assertTrue(self.term_of_service_page.is_displayed())


class TestAboutUs(BaseCase):
    """我的-关于我们-关于我们"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_page_info(self):
        """显示app版本号，技术服务热线，微信公众号"""
        self.main_page.switch_to_mine_page()
        self.mine_page.click_about_us()
        self.assertTrue(self.about_us_page.is_current_version_displayed())
        self.assertTrue(self.about_us_page.is_hotline_displayed())
        self.assertTrue(self.about_us_page.is_wechat_name_displayed())


if __name__ == '__main__':
    unittest.main()
