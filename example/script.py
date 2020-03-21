import paho.mqtt.client as mqtt
import time
import random
import math


# Define sensors min and max values
MIN_TEMPERATURE = -50
MAX_TEMPERATURE = 50
MIN_HUMIDITY = 0
MAX_HUMIDITY = 100
MIN_WIND_DIRECTION = 0
MAX_WIND_DIRECTION = 360
MIN_WIND_INTENSITY = 0
MAX_WIND_INTENSITY = 100
MIN_RAIN_HEIGHT = 0
MAX_RAIN_HEIGHT = 50

# Define MQTT parameters
TOPIC = 'v1/devices/me/telemetry'
IP = '127.0.0.1'
PORT = 1883
ROME_ACCESS_TOKEN = "x13UmzPu4tud5Fq1zLzL"
MILAN_ACCESS_TOKEN = "UqbllktaQM87gMGfAapz"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc, *extra_params):
   print('Connected with result code '+str(rc))



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   print('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))

# Clients setup 
milan_client = mqtt.Client()
milan_client.on_connect = on_connect
milan_client.on_message = on_message
milan_client.username_pw_set(MILAN_ACCESS_TOKEN)
milan_client.connect(IP, PORT, 1)
milan_client.loop_start()


rome_client = mqtt.Client()
rome_client.on_connect = on_connect
rome_client.on_message = on_message
rome_client.username_pw_set(ROME_ACCESS_TOKEN)
rome_client.connect(IP, PORT, 1)
rome_client.loop_start()



# Message sending via MQTT 
while True:
    ############### FIRST STATION
    ###############
    ###############
    payload="{"
    payload+="\"humidity\":" + str(round(random.uniform(MIN_HUMIDITY,MAX_HUMIDITY), 2)) + ","
    payload+="\"temperature\":" + str(round(random.uniform(MIN_TEMPERATURE,MAX_TEMPERATURE), 1)) + ","
    payload+="\"wind direction\":" + str(round(random.uniform(MIN_WIND_DIRECTION,MAX_WIND_DIRECTION), 1)) + ","
    payload+="\"wind intensity\":" + str(round(random.uniform(MIN_WIND_INTENSITY,MAX_WIND_INTENSITY), 2)) + ","
    payload+="\"rain height\":" + str(round(random.uniform(MIN_RAIN_HEIGHT,MAX_RAIN_HEIGHT), 2))
    payload+="}"
    milan_client.publish(TOPIC, payload, 1)
    print("Please check LATEST TELEMETRY field of Milan sensors")
    print(payload)
    ############### SECOND STATION
    ###############
    ###############   
    payload="{"
    payload+="\"humidity\":" + str(round(random.uniform(MIN_HUMIDITY,MAX_HUMIDITY), 2)) + ","
    payload+="\"temperature\":" + str(round(random.uniform(MIN_TEMPERATURE,MAX_TEMPERATURE), 1)) + ","
    payload+="\"wind direction\":" + str(round(random.uniform(MIN_WIND_DIRECTION,MAX_WIND_DIRECTION), 1)) + ","
    payload+="\"wind intensity\":" + str(round(random.uniform(MIN_WIND_INTENSITY,MAX_WIND_INTENSITY), 2)) + ","
    payload+="\"rain height\":" + str(round(random.uniform(MIN_RAIN_HEIGHT,MAX_RAIN_HEIGHT), 2))
    payload+="}"
    rome_client.publish(TOPIC, payload, 1)
    print("Please check LATEST TELEMETRY field of Rome sensors")
    print(payload)
    time.sleep(5)







