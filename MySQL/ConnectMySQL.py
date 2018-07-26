# encoding = utf-8
import pymysql


class MySQL(object):
    def __init__(self, host, port, dbName, username, password, charset):
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
        self.cur.execute("select * from user;")
        # 从查询区域取回所有查询结果
        dataTuple = self.cur.fetchall()
        return dataTuple

    def closeDataBase(self):
        # 数据库清理
        self.cur.close()
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    db = MySQL(host="210.13.50.105", port=30580, dbName="mysql", username="root", password="111111", charset="utf8")
    print(db.getDataFromDataBase())
    db.closeDataBase()