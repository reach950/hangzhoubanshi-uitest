#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""办理事项组件"""

__author__ = 'kejie'

import random
import logging
from lib import AppiumDriver
from page_object.main.main_page import MainPage
from page_object.main.search_page import SearchPage
from page_object.services.library.library_card_password_change_page import LibraryCardPasswordChangePage
from page_object.services.library.library_main_page import LibraryMainPage


class HandleItem:
    handle_status = False
    item_name = '借阅证密码修改'

    main_page = None
    search_page = None
    library_main_page = None
    library_card_password_change_page = None

    # 办件
    @classmethod
    def handle_item(cls, driver, item_name):
        logging.info('开始办件，事项名称：{}'.format(item_name))
        cls.change_library_card_password(driver)
        cls.handle_status = True

    # 办理借阅证密码修改事项
    @classmethod
    def change_library_card_password(cls, driver):
        cls._init_page(driver)
        password = cls._get_random_password()
        logging.info('密码修改为：{}'.format(password))

        cls.main_page.click_search_field()
        cls.search_page.search(cls.item_name)
        cls.search_page.click_item_name_in_search_result(cls.item_name)

        cls.library_card_password_change_page.wait_to_display()
        cls.library_card_password_change_page.change_password(password)
        cls.library_main_page.wait_to_display()

    @classmethod
    def handle_item_without_driver(cls):
        driver = AppiumDriver().get_driver()
        cls._init_page(driver)
        cls.main_page.wait_to_display()
        cls.handle_item(driver, cls.item_name)
        driver.quit()

    @classmethod
    def handle_item_once(cls):
        if cls.handle_status:
            return
        cls.handle_item_without_driver()

    # 获取随机的六位数密码
    @classmethod
    def _get_random_password(cls):
        password = ''
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            password += ch
        return password

    # 初始化页面对象
    @classmethod
    def _init_page(cls, driver):
        cls.main_page = MainPage(driver)
        cls.search_page = SearchPage(driver)
        cls.library_main_page = LibraryMainPage(driver)
        cls.library_card_password_change_page = LibraryCardPasswordChangePage(driver)
