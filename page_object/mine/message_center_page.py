#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""消息中心页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage
from test_case.common_test_step import login


class MessageCenterPage(BasePage):

    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '消息中心')

    # 第一条消息
    first_message_info = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                    '/XCUIElementTypeStaticText[3]')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        if page_title:
            return page_title.is_displayed()
        else:
            return False

    # 获取第一条消息
    def get_first_message_info(self):
        return self.find_element(self.first_message_info).get_attribute('value')
