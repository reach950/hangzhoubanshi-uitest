#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录组件"""

__author__ = 'kejie'

import logging
from lib import AppiumDriver
from page_object.main.main_page import MainPage
from page_object.mine.mine_page import MinePage
from config.login_users import login_users
from page_object.mine.login_page import LoginPage
from page_object.mine.settings_page import SettingsPage


class Login:
    real_name_user = login_users['real_name_user']
    unreal_name_user = login_users['unreal_name_user']
    main_page = None
    mine_page = None
    settings_page = None
    login_page = None

    # 初始化未实名用户登录
    @classmethod
    def init_unreal_name_user_login(cls):
        logging.info('初始化未实名用户登录')
        driver = AppiumDriver().get_driver()
        cls._init_page(driver)

        cls.main_page.wait_to_display()
        cls.main_page.switch_to_mine_page()
        user_status = cls.mine_page.get_user_status()
        if user_status != '未实名用户':
            if cls.mine_page.is_login():
                cls.mine_page.click_settings()
                cls.settings_page.logout()
                cls.main_page.switch_to_mine_page()
            cls.mine_page.click_user_area()
            cls.login_page.login(cls.unreal_name_user['phone_number'], cls.unreal_name_user['password'])
            cls.mine_page.wait_to_display()
        driver.quit()

    # 初始化实名用户登录
    @classmethod
    def init_real_name_user_login(cls):
        logging.info('初始化实名用户登录')
        driver = AppiumDriver().get_driver()
        cls._init_page(driver)

        cls.main_page.wait_to_display()
        cls.main_page.switch_to_mine_page()
        user_name = cls.mine_page.get_username()
        if user_name != cls.real_name_user['user_name']:
            if cls.mine_page.is_login():
                cls.mine_page.click_settings()
                cls.settings_page.logout()
                cls.main_page.switch_to_mine_page()
            cls.mine_page.click_user_area()
            cls.login_page.login(cls.real_name_user['phone_number'], cls.real_name_user['password'])
            cls.mine_page.wait_to_display()
        driver.quit()

    # 调用前请确保用户为未登录状态
    @classmethod
    def user_login(cls, driver, username=real_name_user['phone_number'], password=real_name_user['password']):
        cls._init_page(driver)

        cls.main_page.switch_to_mine_page()
        cls.mine_page.click_user_area()
        cls.login_page.login(username, password)

    # 调用前请确保用户为登录状态
    @classmethod
    def user_logout(cls, driver):
        cls._init_page(driver)

        cls.main_page.switch_to_mine_page()
        cls.mine_page.click_settings()
        cls.settings_page.logout()

    # 初始化页面对象
    @classmethod
    def _init_page(cls, driver):
        cls.main_page = MainPage(driver)
        cls.mine_page = MinePage(driver)
        cls.settings_page = SettingsPage(driver)
        cls.login_page = LoginPage(driver)

    @classmethod
    def user_login_without_driver(cls, username=real_name_user['phone_number'], password=real_name_user['password']):
        driver = AppiumDriver().get_driver()
        cls.user_login(driver, username, password)
        cls.mine_page.wait_to_display()
        driver.quit()

    @classmethod
    def user_logout_without_driver(cls):
        driver = AppiumDriver().get_driver()
        cls.user_logout(driver)
        cls.main_page.wait_to_display()
        driver.quit()
