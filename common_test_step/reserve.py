#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""预约组件"""

__author__ = 'kejie'

import logging
from page_object.main.reserve_subpages.reserve_page import ReservePage
from page_object.main.reserve_subpages.reserve_process_subpages.hangzhou_civic_center_page import HangzhouCivicCenterPage
from page_object.main.reserve_subpages.reserve_process_subpages.housing_provident_funds_page import \
    HousingProvidentFundsPage
from page_object.main.reserve_subpages.reserve_process_subpages.reserve_info_confirm_page import ReserveInfoConfirmPage
from page_object.main.reserve_subpages.reserve_process_subpages.reserve_time_page import ReserveTimePage
from page_object.main.main_page import MainPage
from page_object.main.reserve_subpages.reserve_process_subpages.reserve_success_page import ReserveSuccessPage
from page_object.main.reserve_subpages.reserve_info_query_subpages.activate_reserve_page import ActivateReservePage
from page_object.main.reserve_subpages.reserve_info_query_subpages.reserve_record_page import ReserveRecordPage

reserve_info = {}
main_page = None
reserve_page = None
hangzhou_civic_center_page = None
housing_provident_funds_page = None
reserve_time_page = None
reserve_info_confirm_page = None
reserve_success_page = None
reserve_record_page = None
activate_reserve_page = None


# 获取预约成功的事项，如果没有，就预约一个
def get_reserve_item(driver):
    logging.info('开始获取预约事项')
    _init_page(driver)
    global reserve_info
    if not reserve_info:
        logging.info('没有预约事项，重新预约')
        main_page.scroll_to_cross_stage()
        main_page.open_reserve_page()
        reserve_page.open_hangzhou_civic_center_page()
        hangzhou_civic_center_page.open_housing_provident_funds_page()
        housing_provident_funds_page.click_personal_housing_provident_funds_free()
        reserve_time_page.click_first_reserve_time()
        reserve_info = reserve_info_confirm_page.get_reserve_info()
        reserve_info_confirm_page.confirm_reserve_info()
        reserve_success_page.back_to_reserve_page()
        reserve_page.back_to_index()
    return reserve_info


# 取消预约，调用前需要保证预约列表中有预约成功的记录
def cancel_reserve(driver):
    logging.info('开始取消预约事项')
    _init_page(driver)
    main_page.scroll_to_cross_stage()
    main_page.open_reserve_page()
    reserve_page.open_query_reserve_info_page()
    reserve_record_page.open_first_reserve_detail_page()
    activate_reserve_page.cancel_reserve()
    global reserve_info
    reserve_info = {}


# 初始化页面对象
def _init_page(driver):
    global main_page, reserve_page, hangzhou_civic_center_page, housing_provident_funds_page, reserve_time_page, \
        reserve_info_confirm_page, reserve_success_page, reserve_record_page, activate_reserve_page
    main_page = MainPage(driver)
    reserve_page = ReservePage(driver)
    hangzhou_civic_center_page = HangzhouCivicCenterPage(driver)
    housing_provident_funds_page = HousingProvidentFundsPage(driver)
    reserve_time_page = ReserveTimePage(driver)
    reserve_info_confirm_page = ReserveInfoConfirmPage(driver)
    reserve_success_page = ReserveSuccessPage(driver)
    reserve_record_page = ReserveRecordPage(driver)
    activate_reserve_page = ActivateReservePage(driver)
