#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""appium driver启动的配置信息"""

__author__ = 'kejie'


desired_caps = {
    'automationName': 'XCUITest',  # Xcode8.2以上无UIAutomation,需使用XCUITest
    'platformName': 'iOS',
    'platformVersion': '12.0',
    'deviceName': 'kejie',
    'bundleId': 'com.hzfi.hangzhoubanshi',
    'udid': '3a5a5974b6d66a4c327a6df99de7f7e0e0a00216',
    'newCommandTimeout': 3600,
    # 'startIWDP': True,
    # 'xcodeOrgId': 'VHJLLQ36QB',
    # 'xcodeSigningId': 'iPhone Developer'
}
