#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""资讯详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class NewsDetailPage(BasePage):

    # 杭州发布与杭州办事服务新闻标题
    hzfb_news_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.x == 16 AND rect.y == 108')

    # 杭州日报与杭州网新闻标题
    hzrb_news_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.x == 15 AND rect.y == 115')

    # 获取新闻标题
    def get_news_title(self, source):
        if source in ('杭州发布', '杭州办事服务'):
            return self.find_element(self.hzfb_news_title_loc).get_attribute('name')
        else:
            return self.find_element(self.hzrb_news_title_loc).get_attribute('name')
