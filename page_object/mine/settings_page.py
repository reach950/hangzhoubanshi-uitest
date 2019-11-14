#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""设置页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class SettingsPage(BasePage):
    # 安全退出按钮
    quit_button_loc = (MobileBy.ACCESSIBILITY_ID, '安全退出')

    # 退出登录按钮
    logout_button_loc = (MobileBy.ACCESSIBILITY_ID, '退出登录')

    # 清空缓存
    clear_cache_loc = (MobileBy.ACCESSIBILITY_ID, '清空缓存')

    # 缓存大小
    cache_size_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND rect.width == 61')

    # 清空缓存
    def clear_cache(self):
        self.tap_element(self.clear_cache_loc)
        self.click_alert_button('确定')

    # 登出
    def logout(self):
        self.tap_element(self.quit_button_loc)
        self.tap_element(self.logout_button_loc)

    # 获取缓存空间
    def get_cache_size(self):
        return self.find_element(self.cache_size_loc).get_attribute('value')
