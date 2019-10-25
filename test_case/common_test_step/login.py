#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录组件"""

__author__ = 'kejie'

import functools
import logging
from lib import AppiumDriver
from page_object.index.index_page import IndexPage
from page_object.mine.mine_page import MinePage
from config.login_user import login_user
from page_object.mine.login_page import LoginPage
from page_object.mine.settings_page import SettingsPage

login_state = True
real_name_user = login_user['real_name']


# 初始化登录状态
def init_login_state():
    logging.info('初始化登录状态')
    global login_state
    driver = AppiumDriver().get_driver()
    index_page = IndexPage(driver)
    mine_page = MinePage(driver)

    index_page.wait_to_display()
    index_page.switch_to_mine_page()
    login_state = mine_page.is_login()
    if login_state:
        logging.info('当前app为已登录状态')
    else:
        logging.info('当前app为未登录状态')
    driver.quit()


# 用例执行前是否需要登录
def login(func):
    @functools.wraps(func)
    def _login(self, *args, **kw):
        global login_state
        if not login_state:
            user_login(self.driver)
            self.mine_page.switch_to_index_page()
        return func(self, *args, **kw)

    return _login


# 用例执行前是否需要登出
def logout(func):
    @functools.wraps(func)
    def _logout(self, *args, **kw):
        global login_state
        if login_state:
            user_logout(self.driver)
        return func(self, *args, **kw)

    return _logout


# 调用前请确保用户为未登录状态
def user_login(driver, username=real_name_user['phone_number'], password=real_name_user['password']):
    index_page = IndexPage(driver)
    mine_page = MinePage(driver)
    login_page = LoginPage(driver)

    index_page.switch_to_mine_page()
    mine_page.click_user_area()
    login_page.login(username, password)
    global login_state
    login_state = mine_page.is_displayed()


# 调用前请确保用户为登录状态
def user_logout(driver):
    index_page = IndexPage(driver)
    mine_page = MinePage(driver)
    settings_page = SettingsPage(driver)

    index_page.switch_to_mine_page()
    mine_page.open_settings_page()
    settings_page.logout()
    global login_state
    login_state = False


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
