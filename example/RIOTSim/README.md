### RIOT OS 



Here you can find the C code needed to simulate sensors within **RIOT**.  Values are sent via MQTT-SN to a gateway, previously configured, and then forwarded to our local Mosquitto broker via MQTT; finally they reach ThingsBoard, since we configured Mosquitto as a bridge. 

The code is absolutely trivial and easy to replicate, as you can see in `RIOTSim/main.c`. 