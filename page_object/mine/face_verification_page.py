#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""人脸认证页面"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class FaceVerificationPage(BasePage):
    # 开始刷脸按钮
    start_verify_face_loc = (MobileBy.ACCESSIBILITY_ID, '开始刷脸')

    # 页面是否显示
    def is_displayed(self):
        start_verify_face = self.find_element(self.start_verify_face_loc)
        if start_verify_face:
            return start_verify_face.is_displayed()
        else:
            return False
