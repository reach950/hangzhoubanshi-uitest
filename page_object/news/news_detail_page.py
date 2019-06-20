#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""资讯详情页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class NewsDetailPage(BasePage):

    # 新闻标题
    news_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWebView/**/XCUIElementTypeStaticText[1]')

    # 获取新闻标题
    def get_news_title(self):
        return self.find_element(self.news_title_loc).get_attribute('name')
