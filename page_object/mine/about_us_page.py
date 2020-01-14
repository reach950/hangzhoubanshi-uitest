#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""关于我们页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AboutUsPage(BasePage):
    # 当前版本
    current_version_loc = (MobileBy.ACCESSIBILITY_ID, '当前版本：V1.3.6')

    # 技术服务热线电话
    hotline_loc = (MobileBy.ACCESSIBILITY_ID, '0571-87292733')

    # 微信公众号
    wechat_name_loc = (MobileBy.ACCESSIBILITY_ID, '杭州办事服务')

    # 服务条款
    term_of_service_loc = (MobileBy.ACCESSIBILITY_ID, '《服务条款》')

    # 当前版本是否显示
    def is_current_version_display(self):
        current_version = self.find_element(self.current_version_loc)
        if current_version:
            return current_version.is_displayed()
        else:
            return False

    # 当前热线电话是否显示
    def is_hotline_display(self):
        hotline = self.find_element(self.hotline_loc)
        if hotline:
            return hotline.is_displayed()
        else:
            return False

    # 当前微信公众号是否显示
    def is_wechat_name_display(self):
        wechat_name = self.find_element(self.wechat_name_loc)
        if wechat_name:
            return wechat_name.is_displayed()
        else:
            return False

    # 打开服务条款
    def open_term_of_service(self):
        self.tap_element(self.term_of_service_loc)
