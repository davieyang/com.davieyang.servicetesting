# 用于实现读取Excel数据文件代码封装
# encoding = utf-8
"""
__project__ = 'KeyDri'
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import openpyxl
from openpyxl.styles import Border, Side, Font
import time


class ParseExcel(object):

    def __init__(self):
        self.workBook = None
        self.excelFile = None
        self.font = Font(color=None)
        self.RGBDict = {'red': 'FFFF3030', 'green': 'FF008B00'}

    def loadWorkBook(self, excelPathAndName):
        # 将Excel加载到内存，并获取其workbook对象
        try:
            self.workBook = openpyxl.load_workbook(excelPathAndName)
        except Exception as e:
            raise e
        self.excelFile = excelPathAndName
        return self.workBook

    def getSheetByName(self, sheetName):
        # 根据sheet名获取该sheet对象
        try:
            # sheet = self.workBook.get_sheet_by_name(sheetName)
            sheet = self.workBook[sheetName]
            return sheet
        except Exception as e:
            raise e

    def getSheetByIndex(self, sheetIndex):
        # 根据sheet的索引号获取该sheet对象
        try:
            # sheetname = self.workBook.get_sheet_names()[sheetIndex]
            sheetname = self.workBook.sheetnames[sheetIndex]
        except Exception as e:
            raise e
        # sheet = self.workBook.get_sheet_by_name(sheetname)
        sheet = self.workBook[sheetname]
        return sheet

    def getRowsNumber(self, sheet):
        # 获取sheet中有数据区域的结束行号
        return sheet.max_row

    def getColsNumber(self, sheet):
        # 获取sheet中有数据区域的结束列号
        return sheet.max_column

    def getStartRowNumber(self, sheet):
        # 获取sheet中有数据区域的开始的行号
        return sheet.min_row

    def getStartColNumber(self, sheet):
        # 获取sheet中有数据区域的开始的列号
        return sheet.min_column

    def getRow(self, sheet, rowNo):
        # 获取sheet中某一行，返回的是这一行所有数据内容组成的tuple
        # 下标从1开始，sheet.rows[1]表示第一行
        try:
            # return sheet.rows[rowNo - 1] 因为sheet.rows是生成器类型，不能使用索引
            # 转换成list之后再使用索引，list(sheet.rows)[2]这样就获取到第二行的tuple对象。
            return list(sheet.rows)[rowNo - 1]
        except Exception as e:
            raise e

    def getCol(self, sheet, colNo):
        # 获取sheet中某一列，返回的是这一列所有数据内容组成的tuple
        # 下标从1开始，sheet.columns[1]表示第一列
        try:
            return list(sheet.columns)[colNo - 1]
        except Exception as e:
            raise e

    def getCellOfValue(self, sheet, coordinate = None, rowNo = None, colNo = None):
        # 根据单元格所在的位置索引获取该单元格中的值，下标从1开始
        # sheet.cell(row = 1, column = 1).value，表示excel中的第一行第一列的值
        if coordinate is not None:
            try:
                return sheet.cell(coordinate=coordinate).value
            except Exception as e:
                raise e
        elif coordinate is None and rowNo is not None and colNo is not None:
            try:
                return sheet.cell(row=rowNo, column=colNo).value
            except Exception as e:
                raise e
        else:
            raise Exception("Insufficient Coordinates of cell!")

    def getCellOfObject(self, sheet, coordinate = None, rowNo = None, colNo = None):
        # 获取某个单元格对象，可以根据单元格所在的位置的数字索引，也可以直接根据Excel中单元格的编码及坐标
        # 如getCellOfObject(sheet, coordinate='A1) or getCellOfObject(sheet, rowNo = 1, colNo = 2)

        if coordinate is not None:
            try:
                return sheet.cell(coordinate=coordinate)
            except Exception as e:
                raise e
        elif coordinate is None and rowNo is not None and colNo is not None:
            try:
                return sheet.cell(row=rowNo, column=colNo)
            except Exception as e:
                raise e
        else:
            raise Exception("Insufficient Coordinates of cell!")

    def writeCell(self, sheet, content, coordinate = None, rowNo = None, colNo = None, style=None):
        # 根据单元格在Excel中的编码坐标或者数字索引坐标向单元格中写入数据，下标从1开始
        # 参数style表示字体的颜色的名字，如red，green
        if coordinate is not None:
            try:
                sheet.cell(coordinate=coordinate).value = content
                if style is not None:
                    sheet.cell(coordinate=coordinate).font = Font(color=self.RGBDict[style])
                self.workBook.save(self.excelFile)
            except Exception as e:
                raise e
        elif coordinate is None and rowNo is not None and colNo is not None:
            try:
                sheet.cell(row=rowNo, column=colNo).value = content
                if style is not None:
                    sheet.cell(row=rowNo, column=colNo).font = Font(color=self.RGBDict[style])
                self.workBook.save(self.excelFile)
            except Exception as e:
                raise e
        else:
            raise Exception("Insufficient Coordinates of cell!")

    def writeCellCurrentTime(self, sheet, coordinate = None, rowNo = None, colNo = None):
        # 写入当前时间，下标从1开始
        now = int(time.time())  # 显示为时间戳
        timeArray = time.localtime(now)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        if coordinate is not None:
            try:
                sheet.cell(coordinate=coordinate).value = currentTime
                self.workBook.save(self.excelFile)
            except Exception as e:
                raise e
        elif coordinate is None and rowNo is not None and colNo is not None:
            try:
                sheet.cell(row=rowNo, column=colNo).value = currentTime
                self.workBook.save(self.excelFile)
            except Exception as e:
                raise e


if __name__ == "__main__":
    from Config.VarConfig import dataFilePath163
    pe = ParseExcel()
    pe.loadWorkBook(dataFilePath163)
    print("通过名称获取sheet对象名字：")
    pe.getSheetByName(u"联系人")
    print("通过Index序号获取sheet对象的名字")
    pe.getSheetByIndex(0)
    sheet = pe.getSheetByIndex(0)
    print(type(sheet))
    print(pe.getRowsNumber(sheet))
    print(pe.getColsNumber(sheet))
    cols = pe.getCol(sheet, 1)
    for i in cols:
        print(i.value)
    # 获取第一行第一列单元格内容
    print(pe.getCellOfValue(sheet, rowNo=1, colNo=1))
    pe.writeCell(sheet, u'中国北京', rowNo=11, colNo=11, style='red')
    pe.writeCellCurrentTime(sheet, rowNo=10, colNo=11)

