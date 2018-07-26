# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
from selenium import webdriver


class BrowserEngine(object):
    """定义一个浏览器引擎类"""
    def __init__(self, driver):
        self.driver = driver

    browser_type = "chrome"

    def get_browser(self):
        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == "Chrome":
            driver = webdriver.Chrome()
        elif self.browser_type == "IE":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver


