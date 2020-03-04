#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""消息中心页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MessageCenterPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "消息中心" AND rect.width == 199')

    # 第一条消息
    first_message_info = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                    '/XCUIElementTypeStaticText[3]')

    # 消息列表
    message_list_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTable')

    # 第一条办件消息
    first_handle_message_loc = (MobileBy.ACCESSIBILITY_ID, '办件消息')

    # 第一条预约消息
    first_reserve_message_loc = (MobileBy.ACCESSIBILITY_ID, '预约消息')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 获取第一条消息
    def get_first_message_info(self):
        return self.find_element(self.first_message_info).get_attribute('name')

    # 滑动到第一条办件消息
    def scroll_to_first_handle_message(self):
        self.scroll(loc=self.message_list_loc, name='办件消息')

    # 滑动到第一条预约消息
    def scroll_to_first_reserve_message(self):
        self.scroll(loc=self.message_list_loc, name='预约消息')

    # 点击第一条办件消息
    def click_first_handle_message(self):
        self.tap_element(self.first_handle_message_loc)

    # 点击第一条预约消息
    def click_first_reserve_message(self):
        self.tap_element(self.first_reserve_message_loc)
