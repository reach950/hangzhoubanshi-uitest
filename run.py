#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用例运行入口"""

__author__ = 'kejie'

import unittest
import os
import logging
from datetime import datetime
from lib.HTMLTestRunner import HTMLTestRunner
from test_case.common_test_step.login import init_login_state

# 用例路径
case_path = os.path.join(os.path.abspath(os.curdir), 'test_case')

# 测试报告信息
result_path = os.path.join(os.path.abspath(os.curdir), 'result', datetime.now().strftime("%Y%m%d%H%M%S"))
os.makedirs(result_path)
report_title = '杭州办事服务iOS用例执行报告'
desc = '杭州办事服务iOS用例执行报告'
report_file = os.path.join(result_path, 'HZBSUITestReport.html')
client_log = os.path.join(result_path, 'client.log')


def run_all_case():
    logging.info('开始执行用例')
    all_case = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py')
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(all_case)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename=client_log, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 初始化登录状态
    init_login_state()
    # 执行用例
    run_all_case()
    # 发送测试报告
    # send_mail(report_file)
