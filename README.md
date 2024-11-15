# message_broker

# Start kafka app
1. cd kafka_app
2. git clone https://github.com/confluentinc/kafka-streams-examples.git
3. cd kafka-streams-examples/
4. git checkout 5.1.4-post
5. docker-compose up -d
6. docker-compose exec schema-registry kafka-avro-console-consumer --bootstrap-server kafka:29092 --topic play-events --from-beginning
7. docker-compose exec schema-registry kafka-avro-console-consumer --bootstrap-server kafka:29092 --topic song-feed --from-beginning
8. Update kafka service in docker-compose:
     

    kafka:
        image: confluentinc/cp-enterprise-kafka:5.1.4
        hostname: kafka
        ports:
          - '9092:9092'
          - '29092:29092'
          - '9093:9093'
        depends_on:
          - zookeeper
        environment:
          KAFKA_BROKER_ID: 1
          KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:29092,PLAINTEXT_HOST://0.0.0.0:9092,EXTERNAL://0.0.0.0:9093
          KAFKA_ZOOKEEPER_CONNECT: zookeeper:32181
          KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT,EXTERNAL:PLAINTEXT
          KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
          KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092,EXTERNAL://localhost:9093
          KAFKA_AUTO_CREATE_TOPICS_ENABLE: "false"
          KAFKA_METRIC_REPORTERS: io.confluent.metrics.reporter.ConfluentMetricsReporter
          KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
          CONFLUENT_METRICS_REPORTER_BOOTSTRAP_SERVERS: kafka:29092
          CONFLUENT_METRICS_REPORTER_ZOOKEEPER_CONNECT: zookeeper:32181
          CONFLUENT_METRICS_REPORTER_TOPIC_REPLICAS: 1
          CONFLUENT_METRICS_ENABLE: 'true'
          CONFLUENT_SUPPORT_CUSTOMER_ID: 'anonymous'
        extra_hosts:
          - "moby:127.0.0.1"