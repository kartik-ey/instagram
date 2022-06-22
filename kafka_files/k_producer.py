from confluent_kafka import Producer
from api.resources import constants

if __name__ == '__main__':
    config = constants.KAFKA_PRODUCER_CONFIG

    # Create Producer instance
    producer = Producer(config)

    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    topic = constants.KAFKA_CREATE_BLOG_TOPIC
    producer.produce(topic, 'key', 'msg', callback=delivery_callback)

    topic2 = constants.KAFKA_LOGS
    producer.produce(topic2, 'log', 'msg', callback=delivery_callback)

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
