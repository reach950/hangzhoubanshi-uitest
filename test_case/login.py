#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档注释"""

__author__ = 'kejie'

import functools
from lib import AppiumDriver
from page_object.index.index_page import IndexPage
from page_object.mine.mine_page import MinePage

login_state = True


def init_login_state():
    global login_state
    driver = AppiumDriver().get_driver()
    index_page = IndexPage(driver)
    mine_page = MinePage(driver)
    index_page.switch_to_mine_page()
    login_state = mine_page.is_login()
    driver.quit()


# 用例执行前是否需要登录
def login(is_login):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kw):
            global login_state
            if is_login != login_state:
                if login_state:
                    self.user_logout()
                else:
                    self.user_login()
            return func(self, *args, **kw)
        return wrapper
    return decorator
