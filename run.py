#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用例运行入口"""

__author__ = 'kejie'

import unittest
import os
import logging
from datetime import datetime
from lib.HTMLTestRunner import HTMLTestRunner
from common_test_step.login import Login

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
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        run_real_name_user_case(runner)
        run_unreal_name_user_case(runner)
    logging.info('用例执行结束')


def run_real_name_user_case(runner: 'HTMLTestRunner'):
    Login.init_real_name_user_login()
    test_suite_path = os.path.join(case_path, 'real_name_user')
    test_suite = unittest.defaultTestLoader.discover(test_suite_path, pattern='*_test.py')
    runner.run(test_suite)


def run_unreal_name_user_case(runner: 'HTMLTestRunner'):
    Login.init_unreal_name_user_login()
    test_suite_path = os.path.join(case_path, 'unreal_name_user')
    test_suite = unittest.defaultTestLoader.discover(test_suite_path, pattern='*_test.py')
    runner.run(test_suite)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename=client_log, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 执行用例
    run_all_case()
    # 发送测试报告
    # send_mail(report_file)
