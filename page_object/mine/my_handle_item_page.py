#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的办件页面"""

__author__ = 'kejie'

import datetime
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class MyHandleItemPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "我的办件" AND rect.width == 199')

    # 办件日期
    handle_item_date_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell'
                                                      '/XCUIElementTypeStaticText[`rect.width == 140`]')

    # 第一条办件记录
    first_handle_item_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 第一条办件名称
    first_handle_item_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                            '/XCUIElementTypeStaticText[1]')

    # 第一条办件日期
    first_handle_item_date_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[1]'
                                                            '/XCUIElementTypeStaticText[3]')

    # 办件列表
    handle_item_list_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTable')

    # 获取所有办件的日期
    def get_all_handle_item_date(self):
        handle_item_dates = []
        eles = self.find_elements(self.handle_item_date_loc)
        for ele in eles:
            handle_item_dates.append(ele.get_attribute('name'))
        return handle_item_dates

    # 点击第一条办件记录
    def click_first_handle_item(self):
        self.tap_element(self.first_handle_item_loc)

    # 点击非当天的办件详情
    def click_not_today_handle_item(self):
        date_today = datetime.date.today().strftime('%Y-%m-%d')
        eles = self.find_elements(self.handle_item_date_loc)
        for i in range(len(eles)):
            date = eles[i].get_attribute('name')
            if date_today not in date:
                self.scroll(loc=self.handle_item_list_loc, name=date)
                ele_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[{}]'.format(i + 1))
                self.tap_element(ele_loc)
                break

    # 获取第一条办件的名称
    def get_first_handle_item_name(self):
        return self.find_element(self.first_handle_item_name_loc).get_attribute('name')

    # 获取第一条办件的日期
    def get_first_handle_item_date(self):
        return self.find_element(self.first_handle_item_date_loc).get_attribute('name')

    # 等到页面显示
    def wait_to_display(self):
        self.is_element_exist_by_loc(self.page_title_loc)

    # 评价对话框是否显示
    def is_evaluation_dialog_displayed(self):
        return self.is_element_exist_by_name('评价')
