# encoding = utf-8
"""
测试demo.html
@davieyang
"""
from selenium import webdriver
driver = webdriver.Chrome()

# 通过绝对路径获取元素 定位查询按钮
driver.find_element_by_xpath("/html/body/div/input[@value='查询']")

# 通过相对路径获取元素 定位查询按钮
driver.find_element_by_xpath("//input[@value='查询']")

# 通过索引号定位元素 定位查询按钮
driver.find_element_by_xpath("//input[2]")  # 可用于定位多个，无论页面分了多少层，每层的第一个input都会被定位到

# 通过索引高级定位 定位第二个div下的超链接
driver.find_element_by_xpath("//div[last()]/a")  # div[last()]表示最后一个div元素，last()函数获取的是指定元素的最后的索引号

# 通过索引高级定位 定位第一个div下的超链接
driver.find_element_by_xpath("//div[last()-1]/a")  # 表示倒数第二个div元素

# 通过索引高级定位 定位最前面一个属于div元素的子元素中的input元素
driver.find_element_by_xpath("//div/input[position()<2]")  # position()函数获取当前元素input的位置序列号

# 通过元素属性值定位
driver.find_element_by_xpath("//img[@href='http://www.sogou.com']")
driver.find_element_by_xpath("//div[@name='div2']/input[@name='div2input']")
driver.find_element_by_xpath("//div[@id='div1']/a[@href='http://www.sogou.com']")
driver.find_element_by_xpath("//input[@type='button']")

# 高级应用之模糊匹配
"""
在自动化测试的实施过程中，常常会遇到页面元素的属性值是动态生成的，每次访问属性值都不一样，此类页面元素定位难度大
假如存在属性值中有一部分内容保持不变，则可以使用模糊匹配
"""
# starts-with(str1, str2) 查找属性alt的属性值为div1关键字开始的页面元素
driver.find_element_by_xpath("//img[start-with(@alt, 'div1')]")
# contains(str1, str2)查找属性alt的属性值包含img关键字的页面元素，只包含即可无需考虑位置
driver.find_element_by_xpath("//img[contains(@alt, 'img')]")

# Xpath轴(Axes)定位元素
"""
轴可以定义相对于当前节点的节点集，使用Axes定位方式可以根据在文档树中的元素相对位置关系进行页面元素定位
及：先找到一个相对好定位的元素，让它作为轴，根据它和要定位元素的相对位置关系进行定位
"""

# 选择当前节点的上层父节点 parent:先获取alt属性值为div2-img2的img元素，基于该元素的位置找到它上一级的div元素
driver.find_element_by_xpath("//img[@alt='div2-img2']/parent::div")

# 选择当前节点的下层所有子节点 child: 原理同上 先获取id属性值威div1的div元素，基于该元素的位置找到它下层节点中的img元素
driver.find_element_by_xpath("//div[@id='div1']/child::img")

# 选择当前节点所有上层的节点 ancestor: 基于img元素的位置找到它上级的div元素
driver.find_element_by_xpath("//img[@alt='div2-img2']/ancestor::div")

# 选择当前节点所有下层的节点（子，孙等）descendant: 基于div的位置找到它下级所有节点中的img元素
driver.find_element_by_xpath("//div[@name='div2']/descendant::img")

# 选择在当前节点之后显示的所有节点 following: 基于div的位置，获取它后面节点中的img元素
driver.find_element_by_xpath("div[@id='div1']/following::img")

# 选择当前节点后续所有兄弟节点 following-sibling: 基于超链接的位置找到它后续兄弟节点中的input元素
driver.find_element_by_xpath("//a[@href='http://www.sogou.com']/following-sibling::input")

# 选择当前节点前面的所有节点 preceding: 基于img的位置找到它前面节点中的div元素
driver.find_element_by_xpath("//img[@alt='div2-img2']/preceding::div")

# 选择当前节点前面的所有兄弟节点 preceding-sibling: 基于input的位置，找到它前面同级节点中的第一个超链接元素
driver.find_element_by_xpath("//input[@value='查询']/preceding-sibling::a[1]")

# 通过text()函数获取页面元素的文本并定位元素 如下1和2等价 3和4等价 5和6等价
driver.find_element_by_xpath("//a[text()='搜狗搜索']")
driver.find_element_by_xpath("//a[.='搜狗搜索']")
driver.find_element_by_xpath("//a[contains(., '百度')]")
driver.find_element_by_xpath("//a[contains(test(), '百度')]")
driver.find_element_by_xpath("//a[contains(text(), '百度')]/preceding::div")
driver.find_element_by_xpath("//a[contains(., '百度')]/..")

"""
Xpath运算符欠缺
"""