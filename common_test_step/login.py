#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录组件"""

__author__ = 'kejie'

import functools
import logging
from enum import Enum, unique
from lib import AppiumDriver
from page_object.main.main_page import MainPage
from page_object.mine.mine_page import MinePage
from config.login_users import login_users
from page_object.mine.login_page import LoginPage
from page_object.mine.settings_page import SettingsPage


@unique
class LoginState(Enum):
    # 未登录
    Logout = 1
    # 实名登录
    RealNameLogin = 2
    # 未实名登录
    UnrealNameLogin = 3


current_login_state = LoginState.RealNameLogin
real_name_user = login_users['real_name_user']
unreal_name_user = login_users['unreal_name_user']


# 初始化登录状态
def init_login_state():
    logging.info('初始化登录状态')
    global current_login_state
    driver = AppiumDriver().get_driver()
    main_page = MainPage(driver)
    mine_page = MinePage(driver)

    main_page.wait_to_display()
    main_page.switch_to_mine_page()
    state = mine_page.get_user_state()
    if state == '未登录用户':
        current_login_state = LoginState.Logout
        logging.info('当前app为未登录状态')
    elif state == '未实名用户':
        current_login_state = LoginState.UnrealNameLogin
        logging.info('当前app为已登录状态，登录用户为{}'.format(state))
    elif state == '已实名用户':
        current_login_state = LoginState.RealNameLogin
        logging.info('当前app为已登录状态，登录用户为{}'.format(state))
    driver.quit()


# 用例执行前是否需要登录
def login(param):
    if not isinstance(param, str):
        return login('real_name')(param)
    else:
        def _login(func):
            @functools.wraps(func)
            def wrapper(self, *args, **kwargs):
                global current_login_state
                if param == 'real_name':
                    if current_login_state == LoginState.Logout:
                        user_login(self.driver)
                        self.mine_page.switch_to_main_page()
                    elif current_login_state == LoginState.UnrealNameLogin:
                        user_logout(self.driver)
                        user_login(self.driver)
                        self.mine_page.switch_to_main_page()
                elif param == 'unreal_name':
                    if current_login_state == LoginState.Logout:
                        user_login(self.driver, unreal_name_user['phone_number'], unreal_name_user['password'])
                        self.mine_page.switch_to_main_page()
                    elif current_login_state == LoginState.RealNameLogin:
                        user_logout(self.driver)
                        user_login(self.driver, unreal_name_user['phone_number'], unreal_name_user['password'])
                        self.mine_page.switch_to_main_page()
                return func(self, *args, **kwargs)

            return wrapper

        return _login


# 用例执行前是否需要登出
def logout(func):
    @functools.wraps(func)
    def _logout(self, *args, **kw):
        global current_login_state
        if current_login_state != LoginState.Logout:
            user_logout(self.driver)
        return func(self, *args, **kw)

    return _logout


# 调用前请确保用户为未登录状态
def user_login(driver, username=real_name_user['phone_number'], password=real_name_user['password']):
    main_page = MainPage(driver)
    mine_page = MinePage(driver)
    login_page = LoginPage(driver)

    main_page.switch_to_mine_page()
    mine_page.click_user_area()
    login_page.login(username, password)
    global current_login_state
    is_login = mine_page.is_displayed()
    if is_login:
        state = mine_page.get_user_state()
        if state == '未实名用户':
            current_login_state = LoginState.UnrealNameLogin
        elif state == '已实名用户':
            current_login_state = LoginState.RealNameLogin


# 调用前请确保用户为登录状态
def user_logout(driver):
    main_page = MainPage(driver)
    mine_page = MinePage(driver)
    settings_page = SettingsPage(driver)

    main_page.switch_to_mine_page()
    mine_page.open_settings_page()
    settings_page.logout()
    global current_login_state
    current_login_state = LoginState.Logout
