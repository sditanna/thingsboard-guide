# thingsboard-guide
This repo explains how to create a cloud-based IoT system that collects information from a set of virtual environmental sensors using the MQTT protocol and to create a simple web site to display the data collected from the sensors.



### Thingsboard

The basic approach provides a Python script that generates random  values, which will be suddenly sent via MQTT to our dashboard on ThingsBoard. This guide follows the Thingsboard setup based on **Docker**, which can be accessed on Thingsboard guides, really clear and quick to follow.  All you need of this repository, in this first part, is in the folder **PythonSim**. 

For all details of this guide, from code to back-end, please read the following article on Medium:

https://medium.com/@ditanna.1765243/a-cloud-based-iot-system-using-thingsboard-and-mqtt-protocol-b22929db188c

and here there is a video demonstration of the system:

https://www.youtube.com/watch?v=cuIU4MpKz3g&feature=youtu.be

### RIOT OS Application

In the next step of this guide we will try to collect values with **RIOT OS**,  a real-time multi-threading operating system with a lot of features; you can find all you need about here:
https://github.com/RIOT-OS/RIOT/tree/2019.01-branch

We will also use **MQTT-SN** protocol, a variation of the known MQTT, for Sensor Networks.



LINK

LINK



