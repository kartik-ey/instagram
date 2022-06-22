from random import choice
from confluent_kafka import Producer
from api.resources import constants

if __name__ == '__main__':
    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config = constants.KAFKA_PRODUCER_CONFIG

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    topic = constants.KAFKA_CREATE_BLOG_TOPIC
    producer.produce(topic, 'key', 'msg', callback=delivery_callback)

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
