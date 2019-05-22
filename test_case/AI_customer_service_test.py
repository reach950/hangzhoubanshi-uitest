#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试智能客服"""

__author__ = 'kejie'


import unittest
from test_case.base_case import BaseCase


class TestAICustomerService(BaseCase):

    def setUp(self):
        super().setUp()
        self.search_text = '公积金'
        self.name = '住房公积金是指国家机关、国有企业、城镇集体企业、外商投资企业、城镇私营企业及其他城镇企业、' \
                    '事业单位、民办非企业单位、社会团体（以下统称单位）及其在职职工缴存的长期住房储金。' \
                    '职工个人缴存的住房公积金和职工所在单位为职工缴存的住房公积金，属于职工个人所有'

    def tearDown(self):
        super().tearDown()

    # 测试输入问题获取智能客服的解决方法
    def test_get_solution_by_input_question(self):
        self.index_page.open_AI_customer_service_page()
        self.AI_customer_service_page.search(self.search_text)
        self.assertTrue(self.AI_customer_service_page.check_element_by_name(self.name),
                        '没有显示{}相关的信息'.format(self.search_text))


if __name__ == '__main__':
    unittest.main()
