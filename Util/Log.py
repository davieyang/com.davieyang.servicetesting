# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import logging.config

from Config.VarConfig import parentDirPath

# 读取日志配置文件
logging.config.fileConfig(parentDirPath + u"\Config\Logger.conf")
# 选择第一个日志格式
logger = logging.getLogger("example02")


def debug(message):
    # 定义debug级别日志打印方式
    logger.debug(message)


def info(message):
    # 定义info级别日志打印方式
    logger.info(message)


def warning(message):
    # 定义warning级别日志打印方式
    logger.warning(message)
