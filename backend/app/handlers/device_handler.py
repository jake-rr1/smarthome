# Module for handling device communication
from backend.app.handlers.amqp_handler import AMQPHandler
import sengled

class Thermometer:
    def __init__(self, device_id, amqp_handler):
        self.device_id = device_id
        self.amqp_handler = amqp_handler

    def change_temp(self, request_temp, dupe_id):
        AMQPHandler.send_message(self.amqp_handler, self.device_id, dupe_id, "Changing {} target temperature to {}".format(self.device_id, request_temp))
        messages = AMQPHandler.receive_messages(self.amqp_handler)

        for message in messages:
            print(message)

class Lights:
    def __init__(self, device_id, amqp_handler):
        self.device_id = device_id
        self.amqp_handler = amqp_handler

    def change_lights_state(self, dupe_id, request):
        AMQPHandler.send_message(self.amqp_handler, self.device_id, dupe_id, "Turning {} lights {}".format(self.device_id, request))
        messages = AMQPHandler.receive_messages(self.amqp_handler)

        if messages[0] == "Turning all lights off":
            print(messages[0])



