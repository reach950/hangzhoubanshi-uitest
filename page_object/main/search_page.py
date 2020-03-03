#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""搜索页"""

__author__ = 'kejie'

import time
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class SearchPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSearchField')

    # 搜索按钮
    search_button_loc = (MobileBy.ACCESSIBILITY_ID, 'Search')

    # 智能客服按钮
    ai_service_button_loc = (MobileBy.ACCESSIBILITY_ID, 'kefu')

    # 取消按钮
    cancel_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.width == 29')

    # 热门搜索
    hot_search_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 历史搜索
    search_history_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[2]')

    # 搜索词子定位器
    search_words_child_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeButton')

    # 历史搜索删除按钮
    search_history_delete_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.heigth == 51')

    # 最后一条搜索结果
    last_search_result_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]')

    # 无结果图片
    no_result_image_loc = (MobileBy.ACCESSIBILITY_ID, 'nothing')

    # 无结果文字
    no_result_text_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name BEGINSWITH "抱歉"')

    # 无结果热门事项
    no_result_hot_items_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND rect.width == 345')

    # 搜索结果中服务下的养老保险
    endowment_insurance_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND rect.width == 75')

    # 输入关键字搜索
    def search(self, text):
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)

    # 点击客服按钮
    def click_ai_service_button(self):
        self.tap_element(self.ai_service_button_loc)

    # 点击取消按钮
    def click_cancel_button(self):
        self.tap_element(self.cancel_button_loc)

    # 获取热门搜索的所有关键词
    def get_all_hot_search_words(self):
        search_words = []
        hot_search = self.find_element(self.hot_search_loc)
        hot_search_words = self.find_elements_from_parent_element(hot_search, self.search_words_child_loc)
        for word in hot_search_words:
            search_words.append(word.get_attribute('name'))
        return search_words

    # 滑动到最后一条搜索结果
    def scroll_to_last_search_result(self):
        count = 0
        while not self.is_element_exist_by_loc(self.last_search_result_loc, display=True, wait_display_time=1):
            if count >= 5:
                break
            self.swipe('up')
            time.sleep(0.5)
            count += 1

    # 是否显示无结果页
    def is_no_result_page_display(self):
        return self.is_element_exist_by_loc(self.no_result_image_loc, display=False) and \
               self.is_element_exist_by_loc(self.no_result_text_loc)

    # 获取无结果页的热门事项
    def get_no_result_hot_items(self):
        hot_items = []
        eles = self.find_elements(self.no_result_hot_items_loc)
        for ele in eles:
            hot_items.append(ele.get_attribute('name'))
        return hot_items

    # 点击养老保险
    def click_endowment_insurance(self):
        self.tap_element(self.endowment_insurance_loc)

    # 搜索结果是否包含办事事项
    def is_search_result_contain_handle_item(self, item_name):
        return self.is_element_exist_by_name(item_name)

    # 搜索结果是否包含服务
    def is_search_result_contain_service(self, service_name):
        return self.is_element_exist_by_name(service_name)

    # 搜索结果是否包含预约
    def is_search_result_contain_reserve(self, reserve_name):
        return self.is_element_exist_by_name(reserve_name)

    # 搜索结果是否包含办事指南
    def is_search_result_contain_guide(self, guide_name):
        return self.is_element_exist_by_name(guide_name)

    # 搜索结果是否包含资讯
    def is_search_result_contain_news(self, news_name):
        return self.is_element_exist_by_name(news_name)
