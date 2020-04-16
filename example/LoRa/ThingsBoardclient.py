import paho.mqtt.client as paho  		    				
import os
import json
import time
from datetime import datetime


# Token of device on ThingsBoard
ACCESS_TOKEN = 'LN32l6CgUfVr7SQd5FMM'
# ThingsBoard on localhost                 
broker = "127.0.0.1"
# ThingsBoard port
tb_port = 1883
# ThingsBoard topic
topicTB = "v1/devices/me/telemetry"                    
                                          
# TheThingsNetwork address
hostTTN = 'eu.thethings.network'  
# port on TTN                         
portTTN = 1883            
# topic on TTN                                            
topicTTN = '+/devices/+/up'                    
# name of your application on TTN                   
appTTN = 'iot-sapienza'                                        
# key of your application           
keyTTN = 'ttn-account-v2.7l_xIiAvHyAbKn8iQSiJolrmAmh_iJF-5O5--AoIzLY'  
# name of your device
deviceTTN = 'rome_station'                                         


payload = ""
# function for callback
def on_publish(client,userdata,result):                 
    print("data published to thingsboard \n")
    pass
# connect for TTN
def on_connect(client, userdata, flags, rc) :          
    print ("Connected with result coder " + str(rc))
# on subscribe function    
def on_subscribe(client, userdata, mid, granted_qos) :
    print ("Subscribed")
# message received function
def on_message(client, userdata, message) :
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    payload = json.loads(message.payload)
    temp = payload['payload_fields']
    payload = temp['string'] 
    

# client object
client = paho.Client()      
# function to callback               
client.on_publish = on_publish
# set device access token on thingsboard
client.username_pw_set(ACCESS_TOKEN)
# connection establishment
client.connect(broker, tb_port, keepalive=60)



# Setting up Data Receiver from TTN
datarec = paho.Client()                      
datarec.on_message = on_message                         
datarec.username_pw_set(appTTN, password=keyTTN)     
datarec.on_subscribe = on_subscribe
datarec.connect(hostTTN, portTTN, keepalive=60)      
datarec.subscribe(topicTTN, qos=1)

client.loop_start()

datarec.loop_start()

# 
while (True) :
    while (payload == "") :
        pass

    print("START")
    ret = client.publish(topicTB, payload)
    print ("Payload : " + payload)
    
    print ("\n")
    print ("\n")
    payload == ""