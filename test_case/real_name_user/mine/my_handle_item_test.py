#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试我的办件"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from common_test_step.handle_item import HandleItem


class TestMyHandleItemList(BaseCase):
    """我的-我的办件-办件列表"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def setUpClass(cls) -> None:
        HandleItem.handle_item_once()

    def test_01_sort_by_date(self):
        """办件记录按时间倒序排序"""
        self._open_my_handle_item_page_from_main_page()
        handle_item_dates = self.my_handle_item_page.get_all_handle_item_date()
        for i in range(0, len(handle_item_dates) - 1):
            self.assertTrue(handle_item_dates[i] >= handle_item_dates[i + 1])

    def test_02_click_today_item_to_rate(self):
        """点击当天已办结状态的办件，唤起评价功能"""
        self._open_my_handle_item_page_from_main_page()
        self.my_handle_item_page.click_first_handle_item()
        self.assertTrue(self.my_handle_item_page.is_evaluation_dialog_displayed())

    def test_03_click_item_to_open_detail(self):
        """点击办件记录，跳转到办件详情"""
        self._open_my_handle_item_page_from_main_page()
        self.my_handle_item_page.click_not_today_handle_item()
        self.assertTrue(self.handle_item_detail_page.is_displayed())

    def _open_my_handle_item_page_from_main_page(self):
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_handle_item()
        self.my_handle_item_page.wait_to_display()


if __name__ == '__main__':
    unittest.main()
