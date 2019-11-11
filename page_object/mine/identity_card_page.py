#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""居民身份证页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class IdentityCardPage(BasePage):
    # 居民身份证背景图片
    identity_card_background_image_loc = (MobileBy.ACCESSIBILITY_ID, 'card_BackgroundImage')

    # 页面是否显示
    def is_displayed(self):
        identity_card_background_image = self.find_element(self.identity_card_background_image_loc)
        if identity_card_background_image:
            return identity_card_background_image.is_displayed()
        else:
            return False
