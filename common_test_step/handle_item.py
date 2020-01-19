#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""办理事项组件"""

__author__ = 'kejie'

import random
import time
import logging
from page_object.main.main_page import MainPage
from page_object.main.search_page import SearchPage
from page_object.services.library.library_card_password_change_page import LibraryCardPasswordChangePage
from page_object.services.library.library_main_page import LibraryMainPage

handle_state = False
handle_bug = True


# 获取办件的事项，没有就办理一个
def get_handle_item(driver):
    global handle_state
    item_name = '借阅证密码修改'
    logging.info('获取办件事项：{}'.format(item_name))
    if not handle_state:
        logging.info('未办理{}，重新办理'.format(item_name))
        main_page = MainPage(driver)
        search_page = SearchPage(driver)
        library_main_page = LibraryMainPage(driver)
        library_card_password_change_page = LibraryCardPasswordChangePage(driver)
        password = _get_random_password()
        logging.info('密码修改为：{}'.format(password))

        main_page.open_search_page()
        search_page.search(item_name)
        search_page.click_element_by_name(item_name)
        # 修改密码页面的webview元素在加载过程中可查找，无法使用等待机制，默认等待10秒钟
        time.sleep(10)
        library_card_password_change_page.change_password(password)
        library_main_page.close_page()
        search_page.cancel_search()
        handle_state = True
    return item_name


# 获取随机的六位数密码
def _get_random_password():
    password = ''
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        password += ch
    return password


if __name__ == '__main__':
    print(_get_random_password())
