#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主页"""

__author__ = 'kejie'

import time
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MainPage(BasePage):
    # 首页table
    table_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTable')

    # 智能客服
    ai_service_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                '/XCUIElementTypeOther[3]')

    # 办事指南
    guide_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]')

    # 搜索框
    search_field_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 300')

    # 更多应用
    more_apps_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "更多"')

    # 杭州资讯更多按钮
    hz_news_more_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "更多"')

    # 杭州资讯第一条资讯标题
    hz_news_first_news_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                              '/XCUIElementTypeStaticText[2]')

    # 杭州资讯第一条资讯来源
    hz_news_first_news_source_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                               '/XCUIElementTypeStaticText[3]')
    # 杭州资讯第二条资讯标题
    hz_news_second_news_date_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                              '/XCUIElementTypeStaticText[5]')

    # tabbar-服务
    tabbar_services_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 95`][1]')

    # tabbar-资讯
    tabbar_news_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 95`][2]')

    # tabbar-我的
    tabbar_mine_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 94`][2]')

    # 智能客服小图标
    ai_service_small_icon_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`rect.width == 27`][3]')

    # 区县服务
    district_service_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-2]')

    # 消息按钮
    message_button_loc = (MobileBy.IOS_PREDICATE,
                          'type == "XCUIElementTypeButton" AND name IN {"home msg unread s", "home msg read s"}')

    # 办件展台里的办件时间
    handle_time_loc = (MobileBy.IOS_PREDICATE, 'name == "刚刚" OR name ENDSWITH "分钟前"')

    # 点击办事指南
    def click_guide(self):
        self.tap_element(self.guide_loc)

    # 点击智能客服
    def click_ai_service(self):
        self.tap_element(self.ai_service_loc)

    # 点击智能客服小图标
    def click_ai_service_small_icon(self):
        self.swipe('up')
        self.tap_element(self.ai_service_small_icon_loc)

    # 点击搜索框
    def click_search_field(self):
        self.tap_element(self.search_field_loc)

    # 点击更多应用
    def click_more_apps(self):
        self.tap_element(self.more_apps_loc)

    # 滑动首页到底部资讯展台
    def scroll_to_news(self):
        count = 0
        while not self.is_element_exist_by_loc(self.hz_news_second_news_date_loc, display=True, wait_display_time=1):
            if count >= 5:
                break
            self.swipe('up')
            time.sleep(0.5)
            count += 1

    # 点击杭州资讯更多按钮
    def click_hz_news_more_button(self):
        self.tap_element(self.hz_news_more_button_loc)

    # 获取第一条资讯标题
    def get_first_news_title(self):
        return self.find_element(self.hz_news_first_news_title_loc).get_attribute('name')

    # 获取第一条资讯来源
    def get_first_news_source(self):
        return self.find_element(self.hz_news_first_news_source_loc).get_attribute('name')

    # 点击第一条资讯标题
    def click_first_news_title(self):
        self.tap_element(self.hz_news_first_news_title_loc)

    # 切换到服务页面
    def switch_to_services_page(self):
        self.tap_element(self.tabbar_services_loc)

    # 切换到资讯页面
    def switch_to_news_page(self):
        self.tap_element(self.tabbar_news_loc)

    # 切换到我的页面
    def switch_to_mine_page(self):
        self.tap_element(self.tabbar_mine_loc)

    # 页面是否显示
    def is_displayed(self):
        return self.is_element_exist_by_name('我要咨询', display=False)

    # 等到页面显示
    def wait_to_display(self):
        self.is_element_exist_by_loc(self.message_button_loc)

    # 滑动首页到办件展台
    def scroll_to_handle_item_stage(self, item_name):
        self.scroll(loc=self.table_loc, name=item_name)

    # 点击区县服务
    def click_district_service(self):
        self.tap_element(self.district_service_loc)

    # 滑动首页到区县服务
    def scroll_to_district_service(self):
        self.scroll(loc=self.table_loc, name='区县服务')

    # 办件展台是否包含办件名称
    def is_handle_item_stage_contain_item_name(self, item_name):
        return self.is_element_exist_by_name(item_name, display=False)

    # 办件展台是否包含办件时间
    def is_handle_item_stage_contain_handle_time(self):
        return self.is_element_exist_by_loc(self.handle_time_loc, display=False)

    # 点击办件展台里的办件名称
    def click_item_name_in_handle_item_stage(self, item_name):
        self.click_element_by_name(item_name)
