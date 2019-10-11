#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""全部应用页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AllAppsPage(BasePage):
    # 我的应用编辑按钮
    edit_button_loc = (MobileBy.ACCESSIBILITY_ID, '编辑')

    # 我的应用完成按钮
    finish_button_loc = (MobileBy.ACCESSIBILITY_ID, '完成')

    # 我的应用中最后一个应用的删除按钮
    last_reduce_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                        '/XCUIElementTypeCollectionView/XCUIElementTypeCell[-1]'
                                                        '/XCUIElementTypeOther/XCUIElementTypeButton[1]')

    # 我的应用中最后一个应用的名称
    last_reduce_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                               '/XCUIElementTypeCollectionView/XCUIElementTypeCell[-1]'
                                               '/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 第一个可添加应用的添加按钮
    first_add_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[$type == XCUIElementTypeButton AND '
                                                      'name == "life add"$]/XCUIElementTypeOther'
                                                      '/XCUIElementTypeButton[1]')

    # 第一个可添加应用的名称
    first_add_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[$type == XCUIElementTypeButton AND '
                                                    'name == "life add"$]/XCUIElementTypeOther'
                                                    '/XCUIElementTypeStaticText')

    # 返回首页按钮
    back_to_index_button_loc = (MobileBy.ACCESSIBILITY_ID, '首页')

    # 从我的应用删除最后一个应用
    def reduce_last_app_from_my_apps(self):
        self.tap_element(self.edit_button_loc)
        self.tap_element(self.last_reduce_button_loc)
        self.tap_element(self.finish_button_loc)

    # 获取我的应用中最后一个应用的名称
    def get_last_app_name_from_my_apps(self):
        return self.find_element(self.last_reduce_name_loc).get_attribute('name')

    # 添加第一个可添加应用到我的应用
    def add_app_to_my_apps(self):
        self.tap_element(self.edit_button_loc)
        self.tap_element(self.first_add_button_loc)
        self.tap_element(self.finish_button_loc)

    # 获取第一个可添加应用的名称
    def get_first_added_app_name(self):
        return self.find_element(self.first_add_name_loc).get_attribute('name')

    # 返回首页
    def back_to_index(self):
        self.tap_element(self.back_to_index_button_loc)
