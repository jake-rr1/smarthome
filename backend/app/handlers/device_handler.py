# Module for handling device communication
from backend.app.handlers.amqp_handler import AMQPHandler

class Thermometer:
    def __init__(self, device_id, amqp_handler):
        self.device_id = device_id
        self.amqp_handler = amqp_handler

    def change_temp(self, request_temp):
        AMQPHandler.send_message(self.amqp_handler, "test_group_id", "test_dupe_id", "test message")

class Lights:
    def __init__(self, device_id):
        self.device_id = device_id

    def lights_off_manual(self, request):
        print(request, self.device_id)

    def lights_on_manual(self, request):
        print(request, self.device_id)

    def lights_off_automatic(self, request):
        print(request, self.device_id)

    def lights_on_automatic(self, request):
        print(request, self.device_id)