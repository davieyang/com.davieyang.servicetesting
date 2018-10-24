'''
@Time    : 2018/10/24 10:15
@Author  : 
@Email   : davieyang@qq.com
@File    : VerifyPostgreSQLService.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8
import psycopg2

class VerifyPostgreSQL(object):
    def __init__(self, database, username, password, host, port):
        self.conn = psycopg2.connect(
            database = database,
            user = username,
            password = password,
            host = host,
            port = port
        )
        print("Opened database successfully")
        self.cur = self.conn.cursor()
    def createtable(self):
        self.cur.execute("CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL)")
        self.conn.commit()
        print("Table created successfully")
    def insertdata(self):
        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )")

        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

        self.conn.commit()
        print("Records created successfully")

    def searchdata(self):
        self.cur.execute("SELECT id,name,address,salary from COMPANY")
        rows = self.cur.fetchall()
        for row in rows:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print("SALARY = ", row[3], "\n")
        print("search data successfully")


if __name__ == '__main__':
    db = VerifyPostgreSQL("postgres", "admin", "111111", "210.13.50.105", "31966")
    # db.createtable()
    # db.insertdata()
    db.searchdata()
