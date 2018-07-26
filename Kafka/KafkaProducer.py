# encoding = utf-8
from kafka import KafkaProducer
#创建链接到broker为192.168.110.23:9092的生产者，并命名为producerkafka
producerkafka = KafkaProducer(bootstrap_servers=['210.13.50.105:31754','210.13.50.105:32064','210.13.50.105:31044'])
#定义用生产者发送消息的方法kafkasend()
def kafkasend():
    for i in range(100):
        msg = b"msg%d" % i
        #调用生产者send方法像名称为test的topic发送消息msg
        producerkafka.send('topic01', msg)
        #打印发送消息过程
        print(msg)


if __name__ == '__main__':
    kafkasend()


