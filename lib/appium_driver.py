#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""初始化appium driver"""

__author__ = 'kejie'

from config import desired_caps
import logging
from appium import webdriver


class AppiumDriver:

    APPIUM_SERVER_URL = 'http://127.0.0.1:4723/wd/hub'

    def __init__(self):
        logging.info('初始化appium driver')
        self.driver = webdriver.Remote(self.APPIUM_SERVER_URL, desired_caps)

    def get_driver(self):
        return self.driver
