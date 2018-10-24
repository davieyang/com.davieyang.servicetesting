'''
@Time    : 2018/10/24 10:15
@Author  : 
@Email   : davieyang@qq.com
@File    : VerifyRabbitMQService.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8
import pika

class VerifyRabbitMQ(object):

    def producter(self, username, password, host, port):
        credentials = pika.PlainCredentials(username, password)
        #链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）
        connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/',credentials))
        #创建频道
        channel = connection.channel()
        # 声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，rabbitmq将会自动清除这些消息。如果队列不存在，则创建
        channel.queue_declare(queue='paas')
        #exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        #向队列插入数值 routing_key是队列名 body是要插入的内容

        channel.basic_publish(exchange='',
                          routing_key='paas',
                          body='Paas platform rabbitMQ service verification')
        print("开始队列")
        #缓冲区已经flush而且消息已经确认发送到了RabbitMQ中，关闭链接
        connection.close()


    def consumer(self, username, password, host, port):
        credentials = pika.PlainCredentials(username, password)
        # 连接到rabbitmq服务器
        connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', credentials))
        channel = connection.channel()

        # 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
        channel.queue_declare(queue='wzg')

        # 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        # 告诉rabbitmq使用callback来接收信息
        channel.basic_consume(callback,
                              queue='paas',
                              no_ack=True)
        # no_ack=True表示在回调函数中不需要发送确认标识

        print(' [*] Waiting for messages. To exit press CTRL+C')

        # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
        channel.start_consuming()