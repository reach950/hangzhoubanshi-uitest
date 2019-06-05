#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""appium driver启动的配置信息"""

__author__ = 'kejie'


desired_caps = {
    'automationName': 'XCUITest',  # Xcode8.2以上无UIAutomation,需使用XCUITest
    'platformName': 'iOS',
    'platformVersion': '11.4.1',
    'deviceName': '张彬的 iPhone',
    'bundleId': 'com.hzfi.hangzhoubanshi',
    'udid': '89944f20660db25e2ae01d5242a2032e38cb384a',
    'newCommandTimeout': 3600,
    # 'startIWDP': True,
    'xcodeOrgId': '9728DCQYYU',
    'xcodeSigningId': 'iPhone Developer'
}
