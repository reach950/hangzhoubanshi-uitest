#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试预约展台"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.reserve import get_reserve_item


class TestReserveStage(BaseCase):
    """首页-预约展台-预约"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_check_reserve_info_in_index(self):
        """预约成功，首页显示预约信息"""
        reserve_info = get_reserve_item(self.driver)
        self.assertTrue(self.main_page.check_element_by_name(reserve_info['预约事项']))
        self.assertTrue(self.main_page.check_element_by_name('{}月'.format(reserve_info['办事时间'][5:7])))
        self.assertTrue(self.main_page.check_element_by_name(reserve_info['办事时间'][8:10]))
        # self.assertTrue(self.main_page.check_element_by_name(reserve_info['办事时间'][11:]))

    def test_02_click_reserve_stage_to_open_message_center(self):
        """点击预约展台，跳转到消息中心"""
        reserve_info = get_reserve_item(self.driver)
        self.main_page.click_element_by_name(reserve_info['预约事项'])
        self.assertTrue(self.message_center_page.is_displayed())
        message_info = self.message_center_page.get_first_message_info()
        self.assertIn(reserve_info['办事时间'], message_info)
        self.assertIn(reserve_info['办事大厅'], message_info)


if __name__ == '__main__':
    unittest.main()
