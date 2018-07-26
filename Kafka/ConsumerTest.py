# encoding = utf-8
from kafka import KafkaConsumer

#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('my-topic', bootstrap_servers='192.168.110.24:9092')

for msg in consumer:
    print(msg)