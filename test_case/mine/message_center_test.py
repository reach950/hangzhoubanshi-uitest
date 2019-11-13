#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试消息中心"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login
from test_case.common_test_step.handle_item import get_handle_item
from test_case.common_test_step.reserve import get_reserve_item


class TestMessageType(BaseCase):
    """我的-消息中心-消息类型"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_open_handle_item_detail_page(self):
        """点击办件消息，跳转到对应的办件详情页面"""
        item_name = get_handle_item(self.driver)
        self.index_page.switch_to_mine_page()
        self.mine_page.open_message_center()
        self.message_center_page.open_first_handle_detail()
        self.assertTrue(self.handle_item_detail_page.is_displayed())
        self.assertEqual(item_name, self.handle_item_detail_page.get_item_name())

    @login
    def test_02_open_reserve_detail_page(self):
        """点击预约消息，跳转到对应的预约详情页面"""
        reserve_info = get_reserve_item(self.driver)
        self.index_page.switch_to_mine_page()
        self.mine_page.open_message_center()
        self.message_center_page.open_first_reserve_detail()
        if self.activate_reserve_page.is_displayed():
            # 检查激活预约页面的办事时间
            self.assertEqual(self.activate_reserve_page.get_reserve_time(), reserve_info['办事时间'])
            # 检查激活预约页面的预约事项
            self.assertEqual(self.activate_reserve_page.get_reserve_item_name(), reserve_info['预约事项'])
        elif self.reserve_detail_page.is_displayed():
            test_reserve_info = self.reserve_detail_page.get_reserve_info()
            self.assertEqual(reserve_info['预约事项'], test_reserve_info['预约事项'])
            self.assertEqual(reserve_info['办事时间'], test_reserve_info['办事时间'])


if __name__ == '__main__':
    unittest.main()
