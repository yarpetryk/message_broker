from helpers.kafka import Kafka

class Testkafka:
    def test_kafka(self):
        kafka_listener = Kafka(topic='eqiad.mediawiki.recentchange')
        result = kafka_listener.get_kafka_data()
        print(result)