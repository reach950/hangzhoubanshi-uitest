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

    # 实现页面对象单例模式
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(BasePage, cls).__new__(cls)
        return cls._instance

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
    def send_keys(self, loc, value, clear_first=False):
        """

        :param loc:
        :param value:
        :param clear_first:
        :return:
        """
        ele = self.find_element(loc)
        try:
            if clear_first:
                ele.clear()
            ele.set_value(value)
        except WebDriverException:
            logging.error(u'{} 页面中 {} 元素输入文本失败！'.format(self, loc))

    # 重新封装滑动操作
    def swipe(self, direct, loc=None):
        """
        滑动
        :param direct: 滑动方向，只支持up, down, left ,right四个值
        :param loc: 元素定位，空值为滑动屏幕，有值会滑动对应的元素
        :return:
        """
        if loc:
            self.driver.execute_script('mobile: swipe', {'direction': direct, 'element': self.find_element(loc)})
        else:
            self.driver.execute_script('mobile: swipe', {'direction': direct})

    # 重新封装滑动翻页操作
    def scroll(self, loc=None, **scroll_type):
        """
        滑动翻页
        :param scroll_type: 滑动方式，有“name”，“direction”，“predicateString”或“toVisible”四种方式，只能选择一种
            name: 需要执行滚动的子控件的accessibility id
            direction: 'up', 'down', 'left' or 'right'
            predicateString: 需要被执行滚动操作的子控件的NSPredicate定位器
            toVisible: 布尔类型的参数。如果设置为true，则表示要求滚动到父控件中的第一个可见到的子控件
        :param loc: 元素定位，空值为滑动屏幕，有值会滑动对应的元素
        :return:
        """
        if loc:
            if 'name' in scroll_type:
                self.driver.execute_script('mobile: scroll', {'element': self.find_element(loc),
                                                              'name': scroll_type['name']})
            elif 'direction' in scroll_type:
                self.driver.execute_script('mobile: scroll', {'element': self.find_element(loc),
                                                              'direction': scroll_type['direction']})
            elif 'predicateString' in scroll_type:
                self.driver.execute_script('mobile: scroll', {'element': self.find_element(loc),
                                                              'predicateString': scroll_type['predicateString']})
            elif 'toVisible' in scroll_type:
                self.driver.execute_script('mobile: scroll', {'element': self.find_element(loc),
                                                              'toVisible': scroll_type['toVisible']})
        else:
            self.driver.execute_script('mobile: scroll', {'direction': scroll_type['direction']})

    # 重新封装警告框点击操作
    def click_alert_button(self, button_lable, action='accept'):
        """
        警告框处理
        :param button_lable: 警告框按钮的标签文本
        :param action: 按钮处理，只支持accept，dismiss两个值
        :return:
        """
        self.driver.execute_script('mobile: alert', {'action': action, 'buttonLabel': button_lable})

    # 根据name属性检查元素是否存在
    def check_element_by_name(self, name, wait=15):
        loc = (MobileBy.ACCESSIBILITY_ID, name)
        ele = self.find_element(loc, wait)
        if ele:
            return ele.is_displayed()
        else:
            return False

    # 根据name属性点击元素
    def click_element_by_name(self, name):
        loc = (MobileBy.ACCESSIBILITY_ID, name)
        self.tap_element(loc)
