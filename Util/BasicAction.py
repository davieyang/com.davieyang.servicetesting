# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import os
import time
from Util.GetLog import Logger

mylog = Logger(logger='BasePage').getlog()


class BasePage(object):
    def __init__(self, driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()

    def take_screenshot(self):
        """
        截图并保存在根目录下的Screenshots文件夹下
        :param none:
        """
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("开始截图并保存")

        except Exception as e:
            mylog.error("出现异常", format(e))