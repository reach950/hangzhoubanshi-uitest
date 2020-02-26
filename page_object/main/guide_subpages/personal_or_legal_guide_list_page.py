#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""个人（法人）办事指南页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class PersonalOrLegalGuideListPage(BasePage):
    # 第一个事项指南
    first_guide_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 第一个事项指南的名称
    first_guide_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                      '/XCUIElementTypeStaticText[1]')

    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSearchField')

    # 搜索按钮
    search_button_loc = (MobileBy.ACCESSIBILITY_ID, 'Search')

    # 对象筛选
    target_filter_loc = (MobileBy.ACCESSIBILITY_ID, '对象')

    # 确定按钮
    confirm_button_loc = (MobileBy.ACCESSIBILITY_ID, '确定')

    # 儿童青少年
    children_and_adolescents_loc = (MobileBy.ACCESSIBILITY_ID, '儿童青少年')

    # 点击第一个事项指南
    def click_first_guide(self):
        self.tap_element(self.first_guide_loc)

    # 获取第一个事项指南的名称
    def get_first_guide_name(self):
        return self.find_element(self.first_guide_name_loc).get_attribute('value')

    # 输入关键字搜索
    def search(self, text):
        self.tap_element(self.search_field_loc)
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)

    # 页面是否显示
    def is_displayed(self, page_title_name):
        if page_title_name in ['个人办事', '法人办事']:
            return self.check_element_by_name(page_title_name)
        else:
            return False

    # 对象筛选为儿童青少年
    def change_target_to_children_and_adolescents(self):
        self.tap_element(self.target_filter_loc)
        self.tap_element(self.children_and_adolescents_loc)
        self.tap_element(self.confirm_button_loc)
