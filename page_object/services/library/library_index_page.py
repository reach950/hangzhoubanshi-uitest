#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""图书馆主页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class LibraryIndexPage(BasePage):
    # 关闭页面按钮
    close_button_loc = (MobileBy.ACCESSIBILITY_ID, 'icon wrong')

    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "图书馆"')

    # 密码修改
    password_change_loc = (MobileBy.ACCESSIBILITY_ID, '密码修改')

    # 打开密码修改页面
    def open_password_change_page(self):
        self.tap_element(self.password_change_loc)

    # 关闭页面
    def close_page(self):
        self.tap_element(self.close_button_loc)

    # 等到页面显示
    def wait_to_display(self, count=10):
        while not self.find_element(self.page_title_loc).is_displayed():
            if count == 0:
                break
            count -= 1
