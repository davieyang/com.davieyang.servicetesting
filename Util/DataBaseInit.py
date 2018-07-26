# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import pymysql
from Util.Sql import create_database
from Util.Sql import create_table
from Util.Sql import drop_table


class DataBaseInit(object):
    def __init__(self, host, port, dbName, username, password, charset):
        self.host = host
        self.port = port
        self.db = dbName
        self.user = username
        self.password = password
        self.charset = charset

    def create(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                charset=self.charset
            )
            cur = conn.cursor()
            cur.execute(create_database)
            conn.select_db("davieyang")
            cur.execute(drop_table)
            cur.execute(create_table)
            '''
            cur.execute("drop database if exists davieyang")   #如果davieyang数据库存在则删除  
            cur.execute("create database davieyang")   #新创建一个数据库davieyang  
            cur.execute("use davieyang")         #选择davieyang这个数据库  
            # sql 中的内容为创建一个名为testdata的表  
            sql = """create table testdata(id BIGINT,name VARCHAR(20),age INT DEFAULT 1)"""  #()中的参数可以自行设置  
            conn.execute("drop table if exists testdata") # 如果表存在则删除  
            conn.execute(sql)# 创建表    
            # 删除  
            # conn.execute("drop table testdata")  
            conn.close()# 关闭游标连接  
            connect.close()# 关闭数据库服务器连接 释放内存  
            '''
        except pymysql.Error as e:
            raise e
        else:
            cur.close()
            conn.commit()
            conn.close()
            print(u"创建数据库和表成功")

    def insertDatas(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                db=self.db,
                user=self.user,
                password=self.password,
                charset=self.charset
            )
            cur = conn.cursor()
            sql = "insert into testdata(bookname, author) values(%s, %s);"
            cur.executemany(sql, [('selenium xml DataDriven', 'davieyang'),
                                    ('selenium excel DataDriven', 'davieyang'),
                                    ('selenium ddt data list', 'davieyang')])
        except pymysql.Error as e:
            raise e
        else:
            conn.commit()
            print(u"初始数据插入成功")
            cur.execute("select * from testData;")
            for i in cur.fetchall():
                print(i[1], i[2])
            cur.close()
            conn.close()


if __name__ == '__main__':
    '''
    db = DataBaseInit(host="localhost", port=3306, dbName="davieyang", username="root", password="root",
                      charset="utf8")
    db.create()
    db.insertDatas()
    print(u"数据初始化结束")
    '''