# Module for handling AMQP communication

# backend/app/handlers/amqp_handler.py

import boto3

class AMQPHandler:
    # initialize amqp handler and set queue url
    def __init__(self, queue_url):
        self.sqs = boto3.client('sqs')
        self.queue_url = queue_url

    # function to send messages to queue
    def send_message(self, message_group_id, message_duplication_id, message_body):
        #self.sqs.purge_queue(QueueUrl=self.queue_url)
        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body,
            MessageDeduplicationId=message_duplication_id,
            MessageGroupId=message_group_id
        )
        return response

    # function to receive messages from queue and delete them from queue once processed
    def receive_messages(self):
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            MessageAttributeNames=['All'],
            VisibilityTimeout=30,
            WaitTimeSeconds=0
        )
        messages = response.get('Messages', [])

        if messages:
            # Acknowledge (delete) the message after processing
            receipt_handle = messages[0]['ReceiptHandle']
            self.sqs.delete_message(QueueUrl=self.queue_url, ReceiptHandle=receipt_handle)

        return [message['Body'] for message in messages]
        