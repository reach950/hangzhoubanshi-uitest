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
                                                        '/XCUIElementTypeCollectionView/**/XCUIElementTypeButton[-1]')

    # 我的应用中最后一个应用的名称
    last_reduce_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                      '/XCUIElementTypeCollectionView/**/XCUIElementTypeStaticText[-1]')

    # 第一个可添加应用的添加按钮
    first_add_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "life add"`][1]')

    # 返回首页按钮
    back_to_index_button_loc = (MobileBy.ACCESSIBILITY_ID, '首页')

    # 所有应用
    all_apps_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell'
                                              '/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 最近使用的最后一个应用
    last_recent_use_app_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]')

    # 应用列表
    app_list_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeCollectionView')

    # 点击编辑按钮
    def click_edit_button(self):
        self.tap_element(self.edit_button_loc)

    # 点击完成按钮
    def click_finish_button(self):
        self.tap_element(self.finish_button_loc)

    # 获取我的应用中最后一个应用的名称
    def get_last_app_name_from_my_apps(self):
        return self.find_element(self.last_reduce_name_loc).get_attribute('name')

    # 删除我的应用中最后一个应用
    def delete_last_app_from_my_apps(self):
        self.tap_element(self.last_reduce_button_loc)

    # 添加第一个可添加的应用
    def add_first_app_to_my_apps(self):
        self.tap_element(self.first_add_button_loc)

    # 返回首页
    def back_to_index(self):
        self.tap_element(self.back_to_index_button_loc)

    # 打开最近使用的最后一个应用详情
    def open_last_recent_use_app(self):
        self.tap_element(self.last_recent_use_app_loc)

    # 获取最近使用的第一个应用名称
    def get_first_recent_use_app_name(self):
        apps = self.find_elements(self.all_apps_loc)
        return apps[0].get_attribute('name')

    # 获取最近使用的最后一个应用名称
    def get_last_recent_use_app_name(self):
        apps = self.find_elements(self.all_apps_loc)
        return apps[7].get_attribute('name')

    # 打开一个非最近使用的应用，并返回应用名称
    def open_not_recent_use_app_and_return_app_name(self):
        apps = self.find_elements(self.all_apps_loc)
        recent_use_apps_name = []
        for i, app in enumerate(apps):
            app_name = app.get_attribute('name')
            if i < 8:
                recent_use_apps_name.append(app_name)
            elif app_name not in recent_use_apps_name:
                app_loc = (self.all_apps_loc[0], '{}[{}]'.format(self.all_apps_loc[1], i + 1))
                self.tap_element(app_loc)
                return app_name
