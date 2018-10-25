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

# thrift默认端口是9090
socket = TSocket.TSocket('192.168.0.156', 9090)
socket.setTimeout(5000)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)
socket.open()
print client.getTableNames()
print client.get('test', 'row1', 'cf:a')
