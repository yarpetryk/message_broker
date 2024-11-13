from confluent_kafka import Consumer, KafkaException
import time

class Kafka:
    consumer: Consumer
    kafka_data: list
    init_time: float
    msg_time: float
    def __init__(self, topic):
        self.topic = topic
        self.kafka_data = []
        self.init_time = time.time()
        self.kafka_bootstrap_server = ['kafka:29092']
        self.kafka_group_id = 'console-consumer-63295'
        self.kafka_offset_reset = 'earliest'
        self.__start_kafka_consumer(self.topic)

    def __start_kafka_consumer(self, topic):
        self.consumer = Consumer({
            'bootstrap.servers': self.kafka_bootstrap_server,
            'group.id': self.kafka_group_id,
            'auto.offset.reset': self.kafka_offset_reset
        })
        self.consumer.subscribe([topic])
        while True:
            msg = self.consumer.poll(timeout=1.0)
            print(msg)
            # self.kafka_data.append(msg.value().decode('utf-8'))
            self.kafka_data.append(msg)
            self.msg_time = time.time()
            time_delta = self.msg_time - self.init_time
            if time_delta > 10:
                self.consumer.close()
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
    def get_kafka_data(self):
        if not self.socket_data:
            return False
        else:
            return self.socket_data

kafka_listener = Kafka(topic='play-events')
result = kafka_listener.get_kafka_data()
print(result)