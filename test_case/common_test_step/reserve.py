#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""预约组件"""

__author__ = 'kejie'

from page_object.index.cross_stage_subpages.reserve_page import ReservePage
from page_object.index.cross_stage_subpages.reserve_subpages.hangzhou_civic_center_page import HangzhouCivicCenterPage
from page_object.index.cross_stage_subpages.reserve_subpages.housing_provident_funds_page import \
    HousingProvidentFundsPage
from page_object.index.cross_stage_subpages.reserve_subpages.reserve_info_confirm_page import ReserveInfoConfirmPage
from page_object.index.cross_stage_subpages.reserve_subpages.reserve_time_page import ReserveTimePage
from page_object.index.index_page import IndexPage
from page_object.index.cross_stage_subpages.reserve_subpages.reserve_success_page import ReserveSuccessPage

reserve_info = {}


# 获取预约成功的事项，如果没有，就预约一个
def get_reserve_item(driver):
    global reserve_info
    if not reserve_info:
        index_page = IndexPage(driver)
        reserve_page = ReservePage(driver)
        hangzhou_civic_center_page = HangzhouCivicCenterPage(driver)
        housing_provident_funds_page = HousingProvidentFundsPage(driver)
        reserve_time_page = ReserveTimePage(driver)
        reserve_info_confirm_page = ReserveInfoConfirmPage(driver)
        reserve_success_page = ReserveSuccessPage(driver)

        index_page.scroll_to_cross_stage()
        index_page.open_reserve_page()
        reserve_page.open_hangzhou_civic_center_page()
        hangzhou_civic_center_page.open_housing_provident_funds_page()
        housing_provident_funds_page.click_personal_housing_provident_funds_free()
        reserve_time_page.click_first_reserve_time()
        reserve_info = reserve_info_confirm_page.get_reserve_info()
        reserve_info_confirm_page.click_confirm_reserve_info_button()
        reserve_success_page.click_back_to_index_button()
        reserve_page.back_to_index()
    return reserve_info
