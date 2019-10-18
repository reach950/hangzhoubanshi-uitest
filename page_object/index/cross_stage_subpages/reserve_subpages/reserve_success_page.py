#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""预约成功页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ReserveSuccessPage(BasePage):

    # 查看详情按钮
    view_detail_button_loc = (MobileBy.ACCESSIBILITY_ID, '查看详情')

    # 返回首页按钮
    back_to_index_button_loc = (MobileBy.ACCESSIBILITY_ID, '返回首页')

    # 返回预约首页
    def back_to_reserve_page(self):
        self.tap_element(self.back_to_index_button_loc)
