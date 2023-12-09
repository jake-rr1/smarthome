# Unit tests for the AMQP handler


import sys

import unittest
from unittest.mock import patch
from backend.app.handlers.amqp_handler import AMQPHandler

class TestAMQPHandler(unittest.TestCase):
    @patch('boto3.client')
    def setUp(self, mock_boto3_client):
        self.amqp_handler = AMQPHandler(queue_url="https://sqs.us-west-1.amazonaws.com/832483746143/IoTQueue.fifo")

    @patch('boto3.client')
    def test_send_message(self, mock_boto3_client):
        with patch.object(self.amqp_handler.sqs, 'send_message') as mock_send_message:
            self.amqp_handler.send_message("Test message")
            mock_send_message.assert_called_once_with(QueueUrl="https://sqs.us-west-1.amazonaws.com/832483746143/IoTQueue.fifo", MessageBody="Test message")

    @patch('boto3.client')
    def test_receive_messages(self, mock_boto3_client):
        with patch.object(self.amqp_handler.sqs, 'receive_message') as mock_receive_message:
            mock_receive_message.return_value = {'Messages': [{'Body': 'Test message'}]}
            self.amqp_handler.receive_messages()
            mock_receive_message.assert_called_once_with(
                QueueUrl="https://sqs.us-west-1.amazonaws.com/832483746143/IoTQueue.fifo",
                AttributeNames=['All'],
                MaxNumberOfMessages=1,
                MessageAttributeNames=['All'],
                VisibilityTimeout=0,
                WaitTimeSeconds=0
            )

if __name__ == "__main__":
    unittest.main()
