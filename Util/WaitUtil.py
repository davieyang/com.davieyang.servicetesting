# 用于实现智能等待页面元素的出现
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil(object):

    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def presence_of_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        :param locatorMethod:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            if locationType.lower() in self.locationTypeDict:
                # if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(
                    EC.presence_of_element_located((
                        self.locationTypeDict[locationType.lower()], locatorExpression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def frame_to_be_available_and_switch_to_it(self, locationType, locatorExpression, *args):
        """
        检查frame是否存在，存在则切换进去
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            # 抛出异常信息给上层调用者
            raise e

    def visibility_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素的出现
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception as e:
            raise e


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=r"F:\automation\webdriver\chromedriver.exe")
    driver.get("http://mail.126.com")
    # 实例化WaitUtil类
    waitUtil = WaitUtil(driver)
    # 判断如果id = x-URS-iframe的iframe存在则切换进去
    wf = waitUtil.frame_to_be_available_and_switch_to_it("id", "x-URS-iframe")
    # 等待页面元素xpath = //input[@name='email']的出现
    wv = waitUtil.visibility_element_located("xpath", "//input[@name='email']")
    # 显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
    wp = waitUtil.presence_of_element_located("xpath", "//input[@name='email']")
    driver.quit()
    """
    WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
    '''判断title,返回布尔值'''
    
    WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
    '''判断title，返回布尔值'''
    
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
    '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'su')))
    '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
    
    WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')))
    '''判断元素是否可见，如果可见就返回这个元素'''
    
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
    '''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''
    
    WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.mnav')))
    '''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''
    
    WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'设置'))
    '''判断指定的元素中是否包含了预期的字符串，返回布尔值'''
    
    WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'百度一下'))
    '''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''
    
    #WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
    '''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
    #注意这里并没有一个frame可以切换进去
    
    WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))
    '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
    #注意#swfEveryCookieWrap在此页面中是一个隐藏的元素
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u1']/a[8]"))).click()
    '''判断某个元素中是否可见并且是enable的，代表可点击'''
    driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()
    
    #WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
    '''等待某个元素从dom树中移除'''
    #这里没有找到合适的例子
    
    WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]")))
    '''判断某个元素是否被选中了,一般用在下拉列表'''
    
    WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]"),True))
    '''判断某个元素的选中状态是否符合预期'''
    
    WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be((By.XPATH,"//*[@id='nr']/option[1]"),True))
    '''判断某个元素的选中状态是否符合预期'''
    driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
    
    instance = WebDriverWait(driver,10).until(EC.alert_is_present())
    '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
    print instance.text
    instance.accept()
    """

