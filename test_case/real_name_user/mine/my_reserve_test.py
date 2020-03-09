#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试我的预约"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.reserve import get_reserve_item


class TestMyReserve(BaseCase):
    """我的-我的预约-预约"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_display_government_reserve_and_medical_reserve(self):
        """显示行政预约和医疗预约两个tab页"""
        self._open_my_reserve_page_from_main_page()
        self.assertTrue(self.my_reserve_page.is_contain_government_reserve())
        self.assertTrue(self.my_reserve_page.is_contain_medical_reserve())

    @unittest.skip
    def test_02_check_reserve_info(self):
        """预约事项名称及时间地点显示正确"""
        reserve_info = get_reserve_item(self.driver)
        self._open_my_reserve_page_from_main_page()
        self.assertEqual(self.my_reserve_page.get_first_reserve_name(), reserve_info['预约事项'])
        self.assertEqual(self.my_reserve_page.get_first_reserve_date(), reserve_info['办事时间'])
        self.assertIn(reserve_info['办事大厅'], self.my_reserve_page.get_first_reserve_address())

    def _open_my_reserve_page_from_main_page(self):
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_reserve()
        self.my_reserve_page.wait_to_display()


if __name__ == '__main__':
    unittest.main()
