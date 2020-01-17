#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""如何扫码页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class HowToScanCodePage(BasePage):
    # 引导图
    guide_image_loc = (MobileBy.ACCESSIBILITY_ID, 'reservation_howToScan')

    # 页面是否显示
    def is_displayed(self):
        guide_image = self.find_element(self.guide_image_loc)
        if guide_image:
            return True
        else:
            return False
