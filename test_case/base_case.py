#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
import importlib
import pkgutil
from lib import AppiumDriver
import page_object as po


class BaseCase(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self._init_page()

    def tearDown(self):
        self.driver.quit()

    # 初始化页面对象
    def _init_page(self):
        # 导入所有页面模块
        for module_loader, name, ispkg in pkgutil.walk_packages(po.__path__, '{}.'.format(po.__name__)):
            if not ispkg:
                importlib.import_module(name)
        # 实例化BasePage的子类
        sub_class_list = po.base_page.BasePage.__subclasses__()
        for sub_class in sub_class_list:
            sub_class_instance_name = sub_class.__module__.split('.')[-1]
            self.__dict__[sub_class_instance_name] = sub_class(self.driver)
