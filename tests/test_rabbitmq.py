from helpers.rabbitmq import RabbitMQ


class RabbitMQ:
    def callback(self, ch, method, properties, body):
        print(f"Received message: {body}")

    def test_rabbitmg(self):
        rabbitmq_listener = RabbitMQ()
        try:
            print("Connection to RabbitMQ established successfully.")
            rabbitmq_listener.consume(queue_name='test_queue', callback=self.callback)
        except Exception as e:
            print(f"Failed to establish connection to RabbitMQ: {e}")
        finally:
            rabbitmq_listener.close()