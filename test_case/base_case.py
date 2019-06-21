#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
import importlib
import pkgutil
from lib import AppiumDriver
from config.login_user import login_user
import page_object as po
from page_object.base_page import BasePage
from page_object.index.index_page import IndexPage
from page_object.index.ai_customer_service_page import AICustomerServicePage
from page_object.index.guide_subpages.handle_affairs_guide_select_page import HandleAffairsGuideSelectPage
from page_object.index.guide_subpages.handle_personal_affairs_guide_page import HandlePersonalAffairsGuidePage
from page_object.index.guide_subpages.guide_detail_page import GuideDetailPage
from page_object.index.search_page import SearchPage
from page_object.index.all_apps_page import AllAppsPage
from page_object.index.cross_booth_subpages.handle_page import HandlePage
from page_object.index.cross_booth_subpages.query_page import QueryPage
from page_object.index.cross_booth_subpages.pay_page import PayPage
from page_object.index.cross_booth_subpages.reserve_subpages.hangzhou_civic_center_page import HangzhouCivicCenterPage
from page_object.index.cross_booth_subpages.reserve_subpages. \
    housing_provident_funds_page import HousingProvidentFundsPage
from page_object.index.cross_booth_subpages.reserve_subpages.reserve_time_page import ReserveTimePage
from page_object.index.cross_booth_subpages.reserve_subpages.reserve_info_confirm_page import ReserveInfoConfirmPage
from page_object.index.cross_booth_subpages.reserve_subpages.reserve_success_page import ReserveSuccessPage
from page_object.index.cross_booth_subpages.reserve_info_query_subpages.reserve_record_page import ReserveRecordPage
from page_object.index.cross_booth_subpages.reserve_info_query_subpages.reserve_detail_page import ReserveDetailPage
from page_object.index.cross_booth_subpages.reserve_page import ReservePage
from page_object.index.cross_booth_subpages.reserve_info_query_subpages.activate_reserve_page import ActivateReservePage
from page_object.services.services_page import ServicesPage
from page_object.news.news_page import NewsPage
from page_object.news.news_detail_page import NewsDetailPage
from page_object.mine.mine_page import MinePage
from page_object.mine.login_page import LoginPage
from page_object.mine.settings_page import SettingsPage


class BaseCase(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self._init_page()

    def tearDown(self):
        self.driver.quit()

    # 初始化页面对象
    def _init_page(self):
        # 导入所有页面模块
        for module_loader, name, ispkg in pkgutil.walk_packages(po.__path__, '{}.'.format(po.__name__)):
            if not ispkg:
                importlib.import_module(name)
        # 实例化BasePage的子类
        sub_class_list = po.base_page.BasePage.__subclasses__()
        for sub_class in sub_class_list:
            sub_class_instance_name = sub_class.__module__.split('.')[-1]
            self.__dict__[sub_class_instance_name] = sub_class(self.driver)

    # 调用前请确保用户为未登录状态
    def user_login(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.login_page.login(login_user.phone_number, login_user.password)
        self.mine_page.switch_to_index_page()

    # 调用前请确保用户为登录状态
    def user_logout(self):
        self.index_page.switch_to_mine_page()
        self.mine_page.open_settings_page()
        self.settings_page.logout()

    def init_page(self):
        self.index_page = IndexPage(self.driver)
        self.ai_customer_service_page = AICustomerServicePage(self.driver)
        self.handle_affairs_guide_select_page = HandleAffairsGuideSelectPage(self.driver)
        self.handle_personal_affairs_guide_page = HandlePersonalAffairsGuidePage(self.driver)
        self.guide_detail_page = GuideDetailPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.all_apps_page = AllAppsPage(self.driver)
        self.handle_page = HandlePage(self.driver)
        self.query_page = QueryPage(self.driver)
        self.pay_page = PayPage(self.driver)
        self.reserve_page = ReservePage(self.driver)
        self.hangzhou_civic_center_page = HangzhouCivicCenterPage(self.driver)
        self.housing_provident_funds_page = HousingProvidentFundsPage(self.driver)
        self.reserve_time_page = ReserveTimePage(self.driver)
        self.reserve_info_confirm_page = ReserveInfoConfirmPage(self.driver)
        self.reserve_success_page = ReserveSuccessPage(self.driver)
        self.reserve_record_page = ReserveRecordPage(self.driver)
        self.reserve_detail_page = ReserveDetailPage(self.driver)
        self.activate_reserve_page = ActivateReservePage(self.driver)
        self.services_page = ServicesPage(self.driver)
        self.news_page = NewsPage(self.driver)
        self.news_detail_page = NewsDetailPage(self.driver)
        self.mine_page = MinePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.settings_page = SettingsPage(self.driver)
