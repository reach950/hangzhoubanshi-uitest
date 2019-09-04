#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""资讯页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class NewsPage(BasePage):
    # 杭州发布tab
    hzfb_tab_loc = (MobileBy.IOS_PREDICATE, 'name == "杭州发布" AND rect.width == 64')

    # 发布日期
    publish_date_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND rect.width == 82')

    # 第一条新闻
    first_news_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 450')

    # 第一条新闻标题
    first_news_title_loc = (MobileBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeOther[`rect.width == 450`][1]/XCUIElementTypeOther[1]')

    # 切换到杭州发布tab
    def switch_to_hzfb_tab(self):
        self.tap_element(self.hzfb_tab_loc)

    # 获取所有新闻的发布日期
    def get_all_publish_date(self):
        publish_dates = []
        eles = self.find_elements(self.publish_date_loc)
        for ele in eles:
            publish_dates.append(ele.get_attribute('value'))
        return publish_dates

    # 获取第一条新闻的标题
    def get_first_news_title(self):
        return self.find_element(self.first_news_title_loc).get_attribute('value')

    # 打开第一条新闻
    def open_first_news(self):
        self.tap_element(self.first_news_loc)
