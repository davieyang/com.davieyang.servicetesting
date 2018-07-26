# encoding = utf-8
from kafka import KafkaConsumer
# 定义链接到broker为192.168.110.23:9092 topic为test的消费者
consumerkafka = KafkaConsumer('topic01', bootstrap_servers='210.13.50.105:31754')

# 定义消费者接收生产者消息的方法
def Consumer():
    for message in consumerkafka:
        print(message)
        #print("%s:%d:%d: key=%s value=%s" % (message.topic,message.partition,message.offset,message.key,message.value))


if __name__ == '__main__':
    Consumer()
