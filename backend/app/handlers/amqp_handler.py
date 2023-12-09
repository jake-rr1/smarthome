# Module for handling AMQP communication

# backend/app/handlers/amqp_handler.py

import boto3

class AMQPHandler:
    def __init__(self, queue_url):
        self.sqs = boto3.client('sqs')
        self.queue_url = queue_url

    def send_message(self, message_body):
        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body
        )
        return response

    def receive_messages(self):
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            MessageAttributeNames=['All'],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        messages = response.get('Messages', [])
        return [message['Body'] for message in messages]