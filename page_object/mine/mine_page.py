#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的页面"""

__author__ = 'kejie'

import time
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MinePage(BasePage):
    # 用户区域
    user_area_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 265')

    # 用户姓名
    username_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND rect.width == 192')

    # 用户状态
    user_state_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND rect.width == 60')

    # 设置
    settings_loc = (MobileBy.ACCESSIBILITY_ID, 'M Setting')

    # tabbar-主页
    tabbar_index_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 94`][1]')

    # 我的办件
    my_handle_item_loc = (MobileBy.ACCESSIBILITY_ID, '我的办件')

    # 我的预约
    my_reserve_loc = (MobileBy.ACCESSIBILITY_ID, '我的预约')

    # 我的卡包
    my_card_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeScrollView" AND rect.width == 291')

    # 消息中心
    message_center_loc = (MobileBy.ACCESSIBILITY_ID, '消息中心')

    # 求助反馈
    help_feedback_loc = (MobileBy.ACCESSIBILITY_ID, '求助反馈')

    # 投诉建议
    complaint_suggestion_loc = (MobileBy.ACCESSIBILITY_ID, '投诉建议')

    # 关于我们
    about_us_loc = (MobileBy.ACCESSIBILITY_ID, '关于我们')

    # 获取用户姓名
    def get_username(self):
        return self.find_element(self.username_loc).get_attribute('value')

    # 获取用户状态
    def get_user_state(self):
        return self.find_element(self.user_state_loc).get_attribute('value')

    # 打开设置页面
    def open_settings_page(self):
        self.tap_element(self.settings_loc)

    # 用户是否登录
    def is_login(self):
        return not self.get_username() == '您好' and not self.get_user_state() == '未登录用户'

    # 点击用户区域
    def click_user_area(self):
        self.tap_element(self.user_area_loc)

    # 切换到主页
    def switch_to_index_page(self):
        self.tap_element(self.tabbar_index_loc)

    # 页面是否显示
    def is_displayed(self):
        my_handle_item = self.find_element(self.my_handle_item_loc)
        if my_handle_item:
            return my_handle_item.is_displayed()
        else:
            return False

    # 打开我的办件列表
    def open_my_handle_item(self):
        self.tap_element(self.my_handle_item_loc)

    # 打开我的预约
    def open_my_reserve(self):
        self.tap_element(self.my_reserve_loc)

    # 打开我的卡包
    def open_my_card(self):
        for _ in range(3):
            self.swipe(direct='left', loc=self.my_card_loc)
            time.sleep(1)
        self.tap_element(self.my_card_loc)

    # 打开消息中心
    def open_message_center(self):
        self.tap_element(self.message_center_loc)

    # 打开求助反馈
    def open_help_feedback(self):
        self.tap_element(self.help_feedback_loc)

    # 打开投诉建议
    def open_complaint_suggestion(self):
        self.tap_element(self.complaint_suggestion_loc)

    # 打开关于我们
    def open_about_us(self):
        self.tap_element(self.about_us_loc)
