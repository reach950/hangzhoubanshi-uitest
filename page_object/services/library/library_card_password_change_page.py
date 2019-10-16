#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""借阅证密码修改页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class LibraryCardPasswordChangePage(BasePage):
    # 读者证号
    reader_id = (MobileBy.ACCESSIBILITY_ID, '读者证号')

    # 设置新密码
    set_password_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[1]')

    # 确认新密码
    verify_password_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[2]')

    # 提交按钮
    submit_button_loc = (MobileBy.ACCESSIBILITY_ID, '提交')

    # 修改密码
    def change_password(self, password):
        self.send_keys(self.set_password_loc, password)
        self.send_keys(self.verify_password_loc, password)
        self.tap_element(self.submit_button_loc)

    # 等到页面显示
    def wait_to_display(self, count=10):
        while not self.find_element(self.reader_id).is_displayed():
            if count == 0:
                break
            count -= 1
