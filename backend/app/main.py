# Entry point for the backend application
import sys
sys.path.append("/home/jake-rr1/github/smarthome")

from backend.app.handlers import amqp_handler
from backend.app.handlers.amqp_handler import AMQPHandler
from backend.app.handlers.device_handler import Thermometer

def main():
    amqp_handler = AMQPHandler(queue_url = "https://sqs.us-west-1.amazonaws.com/832483746143/IoTQueue.fifo")

    # allow for user input
    thermometer_id = input("Input thermometer to change: ")
    request_temp = input("Input your requested temperature: ")

    # initialize thermometer device
    thermometer = Thermometer(thermometer_id, amqp_handler)
    # change thermometer temperature
    Thermometer.change_temp(thermometer, request_temp)

if __name__ == "__main__":
    main()