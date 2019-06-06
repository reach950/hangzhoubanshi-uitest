#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主页"""

__author__ = 'kejie'


from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class IndexPage(BasePage):

    # 我要咨询
    wo_yao_zi_xun_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                   '/XCUIElementTypeOther[3]')

    # 办事指南
    ban_shi_zhi_nan_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                     '/XCUIElementTypeOther[4]')

    # 搜索
    search_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 300')

    # 更多应用
    more_app_loc = (MobileBy.ACCESSIBILITY_ID, '更多')

    # 十字展台-我要办理
    wo_yao_ban_li_loc = (MobileBy.ACCESSIBILITY_ID, '我要办理')

    # 十字展台-我要缴费
    wo_yao_jiao_fei_loc = (MobileBy.ACCESSIBILITY_ID, '我要缴费')

    # 十字展台-我要查询
    wo_yao_cha_xun_loc = (MobileBy.ACCESSIBILITY_ID, '我要查询')

    # 十字展台-我要预约
    wo_yao_yu_yue_loc = (MobileBy.ACCESSIBILITY_ID, '我要预约')

    # 打开办事指南页面
    def open_handle_affairs_guide_page(self):
        self.tap_element(self.ban_shi_zhi_nan_loc)

    # 打开智能客服页面
    def open_ai_customer_service_page(self):
        self.tap_element(self.wo_yao_zi_xun_loc)

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
