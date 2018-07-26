# 用于实现将数据设置到剪切板中
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import win32clipboard as c
import win32con

class Clipboard(object):
    """
    模拟windows设置剪切板
    """
    # 读取剪切板
    @staticmethod
    def getText():
        # 打开剪切板
        c.OpenClipboard()
        # 获取剪切板中的数据
        data = c.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪切板
        c.CloseClipboard()
        # 返回剪切板数据给调用者
        return data

    # 设置剪切板内容
    @staticmethod
    def setText(astring):
        # 打开剪切板
        c.OpenClipboard()
        # 清空剪切板
        c.EmptyClipboard()
        # 将数据astring写入剪切板
        c.SetClipboardData(win32con.CF_UNICODETEXT, astring)
        # 关闭剪切板
        c.CloseClipboard()
