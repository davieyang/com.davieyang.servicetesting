# 用于获取当前日期及时间，以及创建异常截图存放目录
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import time, os
from datetime import datetime
from Config.VarConfig import screenPicturesDir


# 获取当前的日期
def getCurrentDate():
    timeUp = time.localtime()
    currentDate = str(timeUp.tm_year) + "-" + str(timeUp.tm_mon) + "-" + str(timeUp.tm_mday)
    return currentDate


# 获取当前时间
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S-%Y')
    return nowTime


# 创建截图存放的路径
def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir, getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName


if __name__ == "__main__":
    print(getCurrentDate())
    print(getCurrentTime())
    print(createCurrentDateDir())
