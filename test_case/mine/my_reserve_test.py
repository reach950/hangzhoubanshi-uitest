#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试我的预约"""

__author__ = 'kejie'

import unittest
import time
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login
from test_case.common_test_step.reserve import get_reserve_item


class TestMyReserve(BaseCase):
    """我的-我的预约-预约"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_display_government_reserve_and_medical_reserve(self):
        """显示行政预约和医疗预约两个tab页"""
        self.index_page.switch_to_mine_page()
        self.mine_page.open_my_reserve()
        time.sleep(5)
        self.assertTrue(self.my_reserve_page.check_element_by_name('行政预约'))
        self.assertTrue(self.my_reserve_page.check_element_by_name('医疗预约'))

    @login
    def test_02_check_reserve_info(self):
        """预约事项名称及时间地点显示正确"""
        reserve_info = get_reserve_item(self.driver)
        self.index_page.switch_to_mine_page()
        self.mine_page.open_my_reserve()
        time.sleep(5)
        self.assertEqual(self.my_reserve_page.get_first_reserve_name(), reserve_info['预约事项'])
        self.assertEqual(self.my_reserve_page.get_first_reserve_date(), reserve_info['办事时间'])
        self.assertIn(reserve_info['办事大厅'], self.my_reserve_page.get_first_reserve_address())


if __name__ == '__main__':
    unittest.main()
