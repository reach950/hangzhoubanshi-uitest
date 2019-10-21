#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务页"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ServicesPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSearchField')

    # 所有应用
    all_apps_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell'
                                              '/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 最近使用的最后一个应用
    last_recent_use_app_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]')

    # 应用列表
    app_list_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeCollectionView')

    # 打开搜索页面
    def open_search_page(self):
        self.tap_element(self.search_field_loc)

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

    # 滑动到应用所在位置
    def scroll_to_app_location(self, app_name):
        self.scroll(loc=self.app_list_loc, name=app_name)
