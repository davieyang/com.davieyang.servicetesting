'''用于解析PageElementLocator.ini中的定位表达式'''
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
from configparser import ConfigParser
# from ConfigParser import ConfigParser
from Config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        # 获取配置文件中指定section下的所有option键值对
        # 并以字典类型返回给调用者
        """
        注意：使用self.cf.items(sectionName)此种方法获取到
        配置文件中的options内容均被转换成小写，如loginPage.frame将被转换成loginpage.frame
        """
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        # 获取指定section下的指定option的值
        value = self.cf.get(sectionName, optionName)
        return value


if __name__ == '__main__':
    ge = ParseConfigFile()
    print(ge.getItemsSection("163mail_login"))
    print(ge.getOptionValue("163mail_login", "loginPage.frame"))
