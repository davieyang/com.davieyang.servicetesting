# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import pymysql
from Util.DataBaseInit import DataBaseInit


class MySQL(object):
    def __init__(self, host, port, dbName, username, password, charset):
        # 进行数据库初始化
        dbInit = DataBaseInit(host, port, dbName, username, password, charset)
        dbInit.create()
        dbInit.insertDatas()
        self.conn = pymysql.connect(
            host=host,
            port=port,
            db=dbName,
            user=username,
            password=password,
            charset=charset
        )
        self.cur = self.conn.cursor()

    def getDataFromDataBase(self):
        # 从数据库中获取数据
        # bookname作为搜索关键词，author作为期望结果
        self.cur.execute("select bookname, author from testdata;")
        # 从查询区域取回所有查询结果
        dataTuple = self.cur.fetchall()
        return dataTuple

    def closeDataBase(self):
        # 数据库清理
        self.cur.close()
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    db = MySQL(
        host="localhost",
        port=3306,
        dbName="davieyang",
        username="root",
        password="root",
        charset="utf8"
    )
    print(db.getDataFromDataBase())
    db.closeDataBase()