#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试办件展台"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.handle_item import HandleItem


class TestHandleItemStage(BaseCase):
    """首页-办件展台-办件"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_check_handle_item_in_main_page(self):
        """办件成功，首页显示办件信息"""
        item_name = HandleItem.get_handle_item(self.driver)
        # 办件名称
        self.assertTrue(self.main_page.is_contain_handle_item_stage(item_name))

    def test_02_click_handle_item_stage_to_open_message_center(self):
        """点击办件展台，跳转到消息中心"""
        item_name = HandleItem.get_handle_item(self.driver)
        self.main_page.scroll_to_handle_item_stage(item_name)
        self.main_page.click_element_by_name(item_name)
        self.assertTrue(self.message_center_page.is_displayed())
        self.assertIn(item_name, self.message_center_page.get_first_message_info())


if __name__ == '__main__':
    unittest.main()
