'''
@Time    : 2018/10/24 10:14
@Author  : 
@Email   : davieyang@qq.com
@File    : VerifyNeo4jService.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8
from py2neo import Graph, Node, Relationship

class VerifyNeo4j(object):


    def neo4j(self, host, username, password):
        graph = Graph(host = host, username = username, password = password)
        temp_node1 = Node(lable="Person", name="node1")
        temp_node2 = Node(lable="Person", name="node2")
        graph.create(temp_node1)
        graph.create(temp_node2)
        node_1_call_node_2 = Relationship(temp_node1, 'CALL', temp_node2)
        node_1_call_node_2['count'] = 1
        node_2_call_node_1 = Relationship(temp_node2, 'CALL', temp_node1)
        graph.create(node_2_call_node_1)
        graph.create(node_1_call_node_2)
        node_1_call_node_2['count'] += 1
        graph.push(node_1_call_node_2)
