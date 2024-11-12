# message_broker

# Start kafka app
1. cd kafka_app
2. git clone https://github.com/confluentinc/kafka-streams-examples.git
3. cd kafka-streams-examples/
4. git checkout 5.1.4-post
5. docker-compose up -d
6. docker-compose exec schema-registry kafka-avro-console-consumer --bootstrap-server kafka:29092 --topic play-events --from-beginning
7. docker-compose exec schema-registry kafka-avro-console-consumer --bootstrap-server kafka:29092 --topic song-feed --from-beginning