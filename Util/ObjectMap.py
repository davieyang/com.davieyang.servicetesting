#  用于实现定位页面元素的公共方法
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""

from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def get_element(driver, locationType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locationType, value=locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个页面元素对象
def get_elements(driver, locationType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30)
        return elements.until(lambda x: x.find_elements(by=locationType, value=locatorExpression))
    except Exception as e:
        raise e


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=r"D:\seleniumWithPython\Drivers\chromedriver.exe")
    driver.get("http://www.baidu.com")
    # 获取locationType=id and locatorExpression=kw的页面元素
    serachBox = get_element(driver, "id", "kw")
    # 打印locationType=id and locatorExpression=kw的页面元素的tag_name属性
    print(serachBox.tag_name)
    # 获取locationType=tag name and locatorExpression=a所有的页面元素
    aList = get_elements(driver, "tag name", "a")
    # 打印locationType=tag name and locatorExpression=a所有的页面元素的所有属性
    print(aList)
    driver.quit()
