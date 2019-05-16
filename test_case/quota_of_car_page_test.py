#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档注释"""

__author__ = 'kejie'


import unittest
from time import sleep
from test_case.base_case import BaseCase
from page_object.index_page import IndexPage


class TestQuotaOfCarPage(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_open_quota_of_page(self):
        self.index_page = IndexPage(self.driver)
        self.index_page.open_quota_of_car_page()
        sleep(10)


if __name__ == '__main__':
    unittest.main()
