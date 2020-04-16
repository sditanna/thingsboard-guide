# thingsboard-guide
This repository contains all the necessary to make some funny IoT things. It has been created for academic purposes: the Internet of Things course 2020



### 1 - Thingsboard

The basic approach provides a Python script that generates random  values, which will be suddenly sent via MQTT to our dashboard on ThingsBoard. This guide follows the Thingsboard setup based on **Docker**, which can be accessed on Thingsboard guides, really clear and quick to follow.  All you need of this repository, in this first part, is in the folder **PythonSim**. 

For all details of this guide, from code to back-end, please follow these links:

-  [Medium article](https://medium.com/@ditanna.1765243/a-cloud-based-iot-system-using-thingsboard-and-mqtt-protocol-b22929db188c)

- [YouTube video](https://www.youtube.com/watch?v=cuIU4MpKz3g&t=8s)



### 2 - RIOT OS Application

In the next step of this guide we will try to collect values with **RIOT OS**,  a real-time multi-threading operating system with a lot of features; you can find all you need about here:
https://github.com/RIOT-OS/RIOT/tree/2019.01-branch

We will also use **MQTT-SN** protocol, a variation of the known MQTT for Sensor Networks, and the Mosquitto broker, which in this case will acts as a bridge.
The additional parts, compared to the first step, are in the folder **RIOTSim**.

For all details of this second step, follow these links:

- [Medium article](https://medium.com/@ditanna.1765243/a-riot-os-application-sending-data-via-mqtt-sn-mqtt-to-thingsboard-41f162e0b9e1?sk=ea2355efda44a3bc633361997674d68e)

- [YouTube video](https://www.youtube.com/watch?v=4jeFf8nW9Ao)



### 3 - LoRAWAN

In this new step we will replace the MQTT protocol and the short-range wireless medium with LoRaWAN and [TheThingsNetwork](https://www.thethingsnetwork.org/). The rest of the system is like the previous tutorial, but we need a new RIOT OS application. All you need is in the folder *example/LoRa*. 

For all details, check the following links:

- [Medium article](https://medium.com/@ditanna.1765243/an-iot-system-built-on-lorawan-riot-os-and-thingsboard-29df6b1a48b2) 

- [YouTube video](https://www.youtube.com/watch?v=w_slNBWrjmM&feature=youtu.be)

