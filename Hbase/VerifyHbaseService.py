'''
@Time    : 2018/10/24 10:14
@Author  : 
@Email   : davieyang@qq.com
@File    : VerifyHbaseService.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase