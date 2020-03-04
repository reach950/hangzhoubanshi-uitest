#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""全部应用页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class AllAppsPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "全部服务"')

    # 搜索框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 搜索按钮
    search_button_loc = (MobileBy.ACCESSIBILITY_ID, 'Search')

    # 智能客服图标
    ai_service_icon_loc = (MobileBy.ACCESSIBILITY_ID, 'allService aiService')

    # 广告图片
    banner_image_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.width == 345')

    # 办理类tab
    handle_tab_loc = (MobileBy.ACCESSIBILITY_ID, '办理类')

    # 缴费类tab
    pay_tab_loc = (MobileBy.ACCESSIBILITY_ID, '缴费类')

    # 查询类tab
    query_tab_loc = (MobileBy.ACCESSIBILITY_ID, '查询类')

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_loc(self.page_title_loc)

    # 输入关键字搜索
    def search(self, text):
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)

    # 点击智能客服图标
    def click_ai_service_icon(self):
        self.tap_element(self.ai_service_icon_loc)

    # 点击广告图片
    def click_banner_image(self):
        self.tap_element(self.banner_image_loc)

    # 切换到办理类tab
    def switch_to_handle_tab(self):
        self.tap_element(self.handle_tab_loc)

    # 切换到缴费类tab
    def switch_to_pay_tab(self):
        self.tap_element(self.pay_tab_loc)

    # 切换到查询类tab
    def switch_to_query_tab(self):
        self.tap_element(self.query_tab_loc)

    # 搜索结果是否包含办理类事项
    def is_search_result_contain_handle_item(self, item_name):
        return self.is_element_exist_by_name(item_name)

    # 搜索结果是否包含缴费类事项
    def is_search_result_contain_pay_item(self, item_name):
        return self.is_element_exist_by_name(item_name, display=False)

    # 搜索结果是否包含查询类事项
    def is_search_result_contain_query_item(self, item_name):
        return self.is_element_exist_by_name(item_name, display=False)

    # 点击事项名称
    def click_item_name(self, item_name):
        self.click_element_by_name(item_name)
