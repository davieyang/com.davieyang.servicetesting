# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 18:52
# @Author  : 
# @Email   : davieyang@qq.com
# @File    : ApplicationIO.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time


class ApplicaitonIO(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url1 = 'http://duantest0.tpaas.youedata.com/hello'
        self.url2 = 'http://192.168.0.46:32680/hello'
        self.url3 = 'http://210.13.50.105:32680/hello'

    def test_io(self):
        for i in range(1, 1000000):
            self.driver.get(self.url1)
            #  time.sleep(1)
            #  self.driver.get(self.url2)
            #  self.driver.get(self.url3)


if __name__ == '__main__':
    unittest.main()
