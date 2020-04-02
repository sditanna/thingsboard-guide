### RIOT OS 



Here you can find the C code needed to simulate sensors within **RIOT**.  Values are sent via MQTT-SN to a gateway, previously configured, and then forwarded to our local Mosquitto broker via MQTT; finally they reach ThingsBoard, since we configured Mosquitto as a bridge. 

The code is absolutely trivial and easy to replicate, as you can see in `RIOTSim/main.c`. 



Main steps to have a working RIOT system in the following.

### Setting up RIOT `native`

When running this example under native, we must configure some global addresses, as the RSMB doesn't seems to be able to handle link-local addresses. So for a single RIOT native instance, we can do the following:

1. Setup `tap` and `tapbr` devices using RIOT's `tapsetup` script:

```
sudo ./RIOTDIR/dist/tools/tapsetup/tapsetup
```

1. Assign a site-global prefix to the `tapbr0` interface:

```
sudo ip a a fec0:affe::1/64 dev tapbr0
```

1. Assign a site-global address with the same prefix within the RIOT `native` instance (open first with `BOARD=native make term`):

```
ifconfig 5 add fec0:affe::99
```

## Usage

This example maps all available MQTT-SN functions to shell commands. Simply type `help` to see the available commands. The most important steps are explained below:

- To connect to a broker, use the `con` command:

```
con fec0:affe::1 1885
```

- To subscribe to a topic, run `sub` with the topic name as parameter, e.g.

```
sub hello/world
```

- For publishing, use the `pub` command:

```
pub hello/world "One more beer, please."
```