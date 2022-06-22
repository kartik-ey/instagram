from confluent_kafka import Consumer
from api.resources import constants

config = constants.KAFKA_CONSUMER_CONFIG
consumer = Consumer(config)

topic = [constants.KAFKA_CREATE_BLOG_TOPIC, constants.KAFKA_LOGS]
consumer.subscribe(topic)

# Poll for new messages from Kafka and print them.
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting...")
        elif msg.error():
            print("ERROR: ", msg.error())
        else:
            # Extract the (optional) key and value, and print.

            print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

except KeyboardInterrupt:
    print('keyboard interrupted')
finally:
    # Leave group and commit final offsets
    consumer.close()
