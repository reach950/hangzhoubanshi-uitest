#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""办理事项组件"""

__author__ = 'kejie'

import random
from page_object.index.index_page import IndexPage
from page_object.index.search_page import SearchPage
from page_object.services.library.library_card_password_change_page import LibraryCardPasswordChangePage
from page_object.services.library.library_index_page import LibraryIndexPage

handle_state = False


# 获取办件的事项，没有就办理一个
def get_handle_item(driver):
    global handle_state
    item_name = '借阅证密码修改'
    if not handle_state:
        index_page = IndexPage(driver)
        search_page = SearchPage(driver)
        library_index_page = LibraryIndexPage(driver)
        library_card_password_change_page = LibraryCardPasswordChangePage(driver)
        password = _get_random_password()

        index_page.open_search_page()
        search_page.search(item_name)
        search_page.click_element_by_name(item_name)
        library_card_password_change_page.change_password(password)
        library_index_page.close_page()
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
