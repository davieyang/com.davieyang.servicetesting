# encoding = utf-8
import time
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers ='192.168.110.23:9092')
# Assign a topic
topic = 'test'


def test():
    print('begin')
    n = 1
    while (n<=100):
        producer.send(topic, b'str(n)')
        print("send" + str(n))
        n += 1
        time.sleep(0.5)
    print('done')


if __name__ == '__main__':
    test()
