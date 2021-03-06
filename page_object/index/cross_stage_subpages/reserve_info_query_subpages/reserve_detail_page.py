#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""预约详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ReserveDetailPage(BasePage):

    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'name == "预约详情" AND rect.width == 199')

    # 姓名
    name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`rect.width == 277`][1]')

    # 身份证号
    identity_card_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`rect.width == 277`][2]')

    # 手机号
    phone_number_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`rect.width == 277`][3]')

    # 办事大厅
    reserve_address_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`rect.width == 277`][4]')

    # 预约事项
    reserve_affair_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`rect.width == 277`][5]')

    # 办事时间
    reserve_time_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`rect.width == 277`][6]')

    # 获取预约信息
    def get_reserve_info(self):
        reserve_info_dict = {
            '姓名': self.find_element(self.name_loc).get_attribute('value'),
            '身份证号': self.find_element(self.identity_card_loc).get_attribute('value'),
            '手机号': self.find_element(self.phone_number_loc).get_attribute('value'),
            '办事大厅': self.find_element(self.reserve_address_loc).get_attribute('value'),
            '预约事项': self.find_element(self.reserve_affair_name_loc).get_attribute('value'),
            '办事时间': self.find_element(self.reserve_time_loc).get_attribute('value')
        }
        return reserve_info_dict

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        if page_title:
            return page_title.is_displayed()
        else:
            return False
