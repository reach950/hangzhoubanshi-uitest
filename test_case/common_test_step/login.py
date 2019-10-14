#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录组件"""

__author__ = 'kejie'

import functools
from lib import AppiumDriver
from page_object.index.index_page import IndexPage
from page_object.mine.mine_page import MinePage

login_state = True


# 初始化登录状态
def init_login_state():
    global login_state
    driver = AppiumDriver().get_driver()
    index_page = IndexPage(driver)
    mine_page = MinePage(driver)
    index_page.wait_to_display()
    index_page.switch_to_mine_page()
    login_state = mine_page.is_login()
    driver.quit()


# 用例执行前是否需要登录
def login(func):
    @functools.wraps(func)
    def _login(self, *args, **kw):
        global login_state
        if not login_state:
            self.user_login()
        return func(self, *args, **kw)

    return _login


# 用例执行前是否需要登出
def logout(func):
    @functools.wraps(func)
    def _logout(self, *args, **kw):
        global login_state
        if login_state:
            self.user_logout()
        return func(self, *args, **kw)

    return _logout


def log(text):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print(text)
            func = fn(*args, **kwargs)
            print('%s executed in %s ms' % (fn.__name__))
            return func

        return wrapper

    decorator = decorator if isinstance(text, str) else decorator(text)
    return decorator
