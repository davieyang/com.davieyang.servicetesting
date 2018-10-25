'''
@Time    : 2018/10/24 10:14
@Author  : 
@Email   : davieyang@qq.com
@File    : VerifyHiveService.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8

import pyhs2
import xlrd
import xlwt


class HiveClient:
    def __init__(self, db_host, user, password, database, port=10000, authMechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  authMechanism=authMechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )

    def query(self, sql):

        """
        query
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetch()

    def close(self):
        """
        close connection
        """
        self.conn.close()

    def writeXlwt(filename,result):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('sheel1')
        for i in range(len(result)+1):
            if i == 0:
                sheet1.row(i).write(0, u'日期')
                sheet1.row(i).write(1, u'小时')
                sheet1.row(i).write(2, u'楼层')
                sheet1.row(i).write(3, u'店铺号')
                sheet1.row(i).write(4, u'店铺名称')
                sheet1.row(i).write(5, u'人数')
            else:
                for a in range(len(result[i-1])):
                    sheet1.row(i).write(a,result[i-1][a])
        book.save(filename)


if __name__ == '__main__':
    hive_client = HiveClient(db_host='192.168.14.44', port=10000, user='hive', password='hive',database='test', authMechanism='PLAIN')
    sql = 'select * from test limit 10'
    result = hive_client.query(sql)