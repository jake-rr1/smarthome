# Entry point for the backend application
import sys
sys.path.append("/home/jake-rr1/github/smarthome")

from backend.app.handlers import amqp_handler
from backend.app.handlers.amqp_handler import AMQPHandler

amqp_handler = AMQPHandler(queue_url = "https://sqs.us-west-1.amazonaws.com/832483746143/IoTQueue.fifo")
AMQPHandler.send_message(amqp_handler, "test_group_id2", "test_dupe_id", "test message")
message_received = AMQPHandler.receive_messages(amqp_handler)

print(message_received)

