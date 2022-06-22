PROJECT_NAME = 'Instagram'
DEBUG = True
VERSION = '1.2'
KAFKA_PRODUCER_CONFIG = {'bootstrap.servers': 'localhost:9092'}
KAFKA_CONSUMER_CONFIG = {'bootstrap.servers': "localhost:9092", 'group.id': "foo", 'auto.offset.reset': 'smallest'}
KAFKA_CREATE_BLOG_TOPIC = "create_blog"
KAFKA_LOGS = 'log'
# user login, user uploads, user likes
