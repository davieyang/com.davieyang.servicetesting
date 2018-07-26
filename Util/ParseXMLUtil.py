# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
from xml.etree import ElementTree


class ParseXML(object):
    def __init__(self, xmlPath):
        self.xmlPath = xmlPath

    def getRoot(self):
        # 打开将要解析的XML文件
        tree = ElementTree.parse(self.xmlPath)
        # 获取XML文件的根节点对象，然后返回给调用者
        return tree.getroot()

    def findNodeByName(self, parentNode, nodeName):
        # 通过节点的名字获取节点对象
        nodes = parentNode.findall(nodeName)
        return nodes

    def getNodeofChildText(self, node):
        # 获取节点node下所有子节点的节点名作为key，本节点作为value组成的字典对象
        childrenTextDict = {i.tag: i.text for i in list(node.iter())[1:]}
        # 上面代码等价于
        '''
        childrenTextDict = {}
        for i in list(node.iter())[1:]:
            fhildrenTextDict[i.tag] = i.text
        '''
        return childrenTextDict

    def getDataFromXml(self):
        # 获取XML文档的根节点对象
        root = self.getRoot()
        # 获取根节点下所有名为book的节点对象
        books = self.findNodeByName(root, "book")
        dataList = []
        # 遍历获取到的所有book节点对象
        # 取得需要的测试数据
        for book in books:
            childrenText = self.getNodeofChildText(book)
            dataList.append(childrenText)
        return dataList


if __name__ == "__main__":
    xml = ParseXML(r"F:\seleniumWithPython\TestData\TestData.xml")
    datas = xml.getDataFromXml()
    for i in datas:
        print(i["name"], i["author"])