# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import xlrd


class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum -1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == '__main__':
    excelPath = u"F:\\seleniumWithPython\\TestData\\163邮箱联系人.xlsx"
    sheetName = u"163账号"
    data = ExcelUtil(excelPath, sheetName)
    print(data.dict_data())

# 打开exlce表格，参数是文件路径
# data = xlrd.open_workbook('test.xlsx')

# table = data.sheets()[0]           #  通过索引顺序获取
# table = data.sheet_by_index(0)     #  通过索引顺序获取
# table = data.sheet_by_name(u'Sheet1')  # 通过名称获取

# nrows = table.nrows  # 获取总行数
# ncols = table.ncols  # 获取总列数

#　获取一行或一列的值，参数是第几行
#  print table.row_values(0)  # 获取第一行值
#  print table.col_values(0)  # 获取第一列值