#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的办件详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class HandleItemDetailPage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.ACCESSIBILITY_ID, '办件详情')

    # 事项名称
    item_name_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "办件详情"`]/XCUIElementTypeOther[6]'
                                               '/XCUIElementTypeStaticText')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        if page_title:
            return page_title.is_displayed()
        else:
            return False

    # 获取事项名称
    def get_item_name(self):
        return self.find_element(self.item_name_loc).get_attribute('value')
