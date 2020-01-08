#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主页"""

__author__ = 'kejie'

import time
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class IndexPage(BasePage):
    # 首页table
    table_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTable')

    # 我要咨询
    wo_yao_zi_xun_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                   '/XCUIElementTypeOther[3]')

    # 办事指南
    ban_shi_zhi_nan_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                     '/XCUIElementTypeOther[4]')

    # 搜索
    search_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 300')

    # 全部应用
    more_app_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "更多"')

    # 十字展台-我要办理
    wo_yao_ban_li_loc = (MobileBy.ACCESSIBILITY_ID, '我要办理')

    # 十字展台-我要缴费
    wo_yao_jiao_fei_loc = (MobileBy.ACCESSIBILITY_ID, '我要缴费')

    # 十字展台-我要查询
    wo_yao_cha_xun_loc = (MobileBy.ACCESSIBILITY_ID, '我要查询')

    # 十字展台-我要预约
    wo_yao_yu_yue_loc = (MobileBy.ACCESSIBILITY_ID, '我要预约')

    # 杭州资讯更多按钮
    hz_news_more_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "更多"')

    # 杭州资讯第一条资讯标题
    hz_news_first_news_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                              '/XCUIElementTypeStaticText[2]')

    # 杭州资讯第一条资讯来源
    hz_news_first_news_source_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                               '/XCUIElementTypeStaticText[3]')
    # 杭州资讯第二条资讯标题
    hz_news_third_news_date_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                             '/XCUIElementTypeStaticText[5]')

    # tabbar-服务
    tabbar_services_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 95`][1]')

    # tabbar-资讯
    tabbar_news_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 95`][2]')

    # tabbar-我的
    tabbar_mine_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 94`][2]')

    # 智能客服小图标
    customer_service_small_icon_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`rect.width == 27`][3]')

    # 地区展台
    district_stage_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-2]')

    # 打开办事指南页面
    def open_handle_items_guide_page(self):
        self.tap_element(self.ban_shi_zhi_nan_loc)

    # 点击我要咨询打开智能客服页面
    def open_ai_customer_service_page(self):
        self.tap_element(self.wo_yao_zi_xun_loc)

    # 点击智能客服小图标打开智能客服页面
    def open_ai_customer_service_page_by_small_icon(self):
        self.swipe('up')
        self.tap_element(self.customer_service_small_icon_loc)

    # 打开搜索页面
    def open_search_page(self):
        self.tap_element(self.search_loc)

    # 打开全部应用
    def open_all_apps_page(self):
        self.tap_element(self.more_app_loc)

    # 打开我要办理页面
    def open_handle_page(self):
        self.tap_element(self.wo_yao_ban_li_loc)

    # 打开我要缴费页面
    def open_pay_page(self):
        self.tap_element(self.wo_yao_jiao_fei_loc)

    # 打开我要查询页面
    def open_query_page(self):
        self.tap_element(self.wo_yao_cha_xun_loc)

    # 打开我要预约页面
    def open_reserve_page(self):
        self.tap_element(self.wo_yao_yu_yue_loc)

    # 滑动首页到底部资讯展台
    def scroll_to_news(self):
        count = 0
        while not self.find_element(self.hz_news_third_news_date_loc).is_displayed():
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

    # 打开第一条资讯详情
    def open_first_news_detail(self):
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
        wo_yao_zi_xun = self.find_element(self.wo_yao_zi_xun_loc)
        if wo_yao_zi_xun:
            return wo_yao_zi_xun.is_displayed()
        else:
            return False

    # 等到页面显示
    def wait_to_display(self, count=5):
        while not self.is_displayed():
            if count == 0:
                break
            count -= 1

    # 滑动首页到十字展台
    def scroll_to_cross_stage(self):
        self.scroll(loc=self.table_loc, name='线上预约线下办理')

    # 滑动首页到办件展台
    def scroll_to_handle_item_stage(self, item_name):
        self.scroll(loc=self.table_loc, name=item_name)

    # 打开地区展台
    def open_district_stage(self):
        self.tap_element(self.district_stage_loc)

    # 滑动首页到地区展台
    def scroll_to_district_stage(self):
        self.scroll(loc=self.table_loc, name='地区服务')
