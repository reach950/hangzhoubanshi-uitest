#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
import importlib
from lib import AppiumDriver
from page_object.base_page import BasePage


class BaseCase(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self._init_page()

    def tearDown(self):
        self.driver.quit()

    def _init_page(self):
        sub_class_list = BasePage.__subclasses__()
        for sub_class in sub_class_list:
            sub_class_module_name = sub_class.__module__
            importlib.import_module(sub_class_module_name)
            sub_class_object_name = sub_class_module_name.split('.')[-1]
            self.__dict__[sub_class_object_name] = sub_class(self.driver)
