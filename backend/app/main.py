# Entry point for the backend application
import sys
sys.path.append("/home/jake-rr1/github/smarthome")
import uuid
from backend.app.handlers.amqp_handler import AMQPHandler
from backend.app.handlers.device_handler import Thermometer, Lights

def main():
    amqp_handler = AMQPHandler(queue_url = "https://sqs.us-west-1.amazonaws.com/832483746143/IoTQueue.fifo")

    # ##########################
    # # Thermometer change
    # ##########################
    # # allow for user input
    # thermometer_id = input("Thermostat: ")
    # request_temp = input("Target temperature: ")

    # # initialize thermometer device
    # thermometer = Thermometer(thermometer_id, amqp_handler)
    # dupe_id = str(uuid.uuid4())
    # # change thermometer temperature
    # Thermometer.change_temp(thermometer, request_temp, dupe_id)


    ##########################
    # Manual light change
    ##########################
    lights_id = input("Lights: ")
    request = input("Request: ")
    sengled_username = "jacobroach99@gmail.com"
    sengled_password = "763Ganjsa2313"

    lights = Lights(lights_id, amqp_handler, sengled_password, sengled_username)

    Lights.change_lights_state(lights,lights_id,request)

if __name__ == "__main__":
    #main()
    import sengled
    sengled_username = "jacobroach99@gmail.com"
    sengled_password = "763Ganjsa2313"
    api = sengled.api(
            # The username/password that you used to create your mobile account in
            # the Sengled Home app.
            username=sengled_username,
            password=sengled_password,

            # Optional path to persist the session across multiple process
            # starts and reduce the number of logins.
            session_path="/tmp/sengled.pickle",

            # Prints details of the api request/responses when True, defaults to false.
            debug=True
        )
    
    print(api.get_device_details(refresh=True))
