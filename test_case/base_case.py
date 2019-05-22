#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
from lib import AppiumDriver
import page_object as po


class BaseCase(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self.init_page()

    def tearDown(self):
        self.driver.quit()

    def init_page(self):
        self.index_page = po.IndexPage(self.driver)
        self.AI_customer_service_page = po.AICustomerServicePage(self.driver)
