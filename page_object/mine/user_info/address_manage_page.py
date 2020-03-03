#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""地址管理页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AddressManagePage(BasePage):
    # 新建地址按钮
    create_address_button_loc = (MobileBy.ACCESSIBILITY_ID, '+ 新建地址')

    # 最后一个地址
    last_address_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]')

    # 最后一个地址的用户姓名
    last_address_username_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                           '/XCUIElementTypeStaticText[1]')

    # 最后一个地址的手机号码
    last_address_phone_number_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                               '/XCUIElementTypeStaticText[2]')

    # 最后一个地址的具体位置
    last_address_detail_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                         '/XCUIElementTypeStaticText[3]')

    # 最后一个地址的编辑按钮
    last_address_edit_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                              '/XCUIElementTypeButton[`name == "edit"`]')

    # 删除按钮
    address_delete_button_loc = (MobileBy.ACCESSIBILITY_ID, '删除')

    # 地址为空的图片
    empty_address_image_loc = (MobileBy.ACCESSIBILITY_ID, 'region-icon')

    # 点击新建地址
    def click_create_address_button(self):
        self.tap_element(self.create_address_button_loc)

    # 点击修改最后一个地址
    def click_last_address_edit_button(self):
        self.tap_element(self.last_address_edit_button_loc)

    # 删除最后一个地址
    def delete_last_address(self):
        self.swipe('left', self.last_address_loc)
        self.tap_element(self.address_delete_button_loc)
        self.click_alert_button('删除')

    # 检查地址列表是否为空
    def is_address_list_empty(self):
        return not self.find_element(self.empty_address_image_loc, wait=5)

    # 获取最后一个地址的具体位置
    def get_last_address_detail(self):
        return self.find_element(self.last_address_detail_loc).get_attribute('value')

    # 获取最后一个地址的用户姓名
    def get_last_address_username(self):
        return self.find_element(self.last_address_username_loc).get_attribute('value')

    # 获取最后一个地址的电话号码
    def get_last_address_phone_number(self):
        return self.find_element(self.last_address_phone_number_loc).get_attribute('value')

    # 等到页面显示
    def wait_to_display(self):
        self.is_element_exist_by_loc(self.create_address_button_loc)

    # 地址是否删除
    def is_address_deleted(self, username, phone_number, detail):
        return self.is_element_disappeared_by_name(username, exist=False) and \
               self.is_element_disappeared_by_name(phone_number, exist=False) and \
               self.is_element_disappeared_by_name(detail, exist=False)
