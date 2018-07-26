# 用于实现模拟键盘单个或多个组合键操作
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import win32api
import win32con


class Keyboardkeys(object):
    """
    模拟键盘按键类
    """
    VK_CODE = {
        'enter': 0x0D,
        'ctrl': 0x11,
        'v': 0x56
    }

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(Keyboardkeys.VK_CODE[keyName], 0, 0, 0)

    @staticmethod
    def keyUp(keyName):
        # 释放按键
        win32api.keybd_event(Keyboardkeys.VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        # 模拟单个按键
        Keyboardkeys.keyDown(key)
        Keyboardkeys.keyUp(key)

    @staticmethod
    def twoKey(key1, key2):
        # 模拟两个组合键
        Keyboardkeys.keyDown(key1)
        Keyboardkeys.keyDown(key2)
        Keyboardkeys.keyUp(key2)
        Keyboardkeys.keyUp(key1)

