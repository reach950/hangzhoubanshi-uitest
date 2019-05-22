#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""页面对象的基类"""

__author__ = 'kejie'

import logging
import json
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from appium.webdriver.common.mobileby import MobileBy


class BasePage:

    def __init__(self, appium_driver):
        self.driver = appium_driver  # type:webdriver.Remote

    # 重新封装单个元素定位方法
    def find_element(self, loc, wait=15) -> webdriver.WebElement:
        """

        :param loc:
        :param wait:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element(*loc))
            return element
        except WebDriverException:
            logging.error(u'{} 页面中未能找到 {} 元素！'.format(self, loc))

    # 重新封装一组元素定位方法
    def find_elements(self, loc, wait=15):
        """

        :param loc:
        :param wait:
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_elements(*loc))
            return elements
        except WebDriverException:
            logging.error(u'{} 页面中未能找到 {} 元素！'.format(self, loc))

    # 重新封装元素点击操作
    def tap_element(self, loc):
        """

        :param loc:
        :return:
        """
        ele = self.find_element(loc)
        rect = json.loads(ele.get_attribute('rect'))
        window_size = self.driver.get_window_size()
        ele_x = rect['x']
        ele_y = rect['y']
        ele_width = rect['width']
        ele_height = rect['height']
        window_width = window_size['width']
        window_height = window_size['height']
        x = ele_width / 2 if (ele_x + ele_width) <= window_width else (window_width - ele_x) / 2
        y = ele_height / 2 if (ele_y + ele_height) <= window_height else (window_height - ele_y) / 2
        self.driver.execute_script('mobile: tap', {'x': x, 'y': y, 'element': ele})

    # 重新封装输入操作
    def send_keys(self, loc, value):
        """

        :param loc:
        :param value:
        :return:
        """
        ele = self.find_element(loc)
        try:
            # ele.clear()
            ele.set_value(value)
        except WebDriverException:
            logging.error(u'{} 页面中 {} 元素输入文本失败！'.format(self, loc))

    # 根据name属性检查元素是否存在
    def check_element_by_name(self, name):
        loc = (MobileBy.ACCESSIBILITY_ID, name)
        return self.find_element(loc).is_displayed()
