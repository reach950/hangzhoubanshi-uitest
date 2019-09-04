#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""资讯详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class NewsDetailPage(BasePage):

    # 杭州发布新闻标题
    hzfb_news_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.x == 16 AND rect.y == 108')

    # 获取杭州发布新闻标题
    def get_hzfb_news_title(self):
        return self.find_element(self.hzfb_news_title_loc).get_attribute('name')
