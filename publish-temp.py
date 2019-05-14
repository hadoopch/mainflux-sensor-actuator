#!/usr/bin/env python3
import sys
import time
import paho.mqtt.client as mqtt
import random

#Some Mainflux related variables
broker_address = "53.252.161.120"
broker_port=1883
thing_id = "922ad39f-fcb2-426f-9651-fbde55ce6cc9"
thing_key = "2fbbeb08-eefe-4308-b09c-fa94907a6b28"
datachannel = "8560ef3b-fd54-462c-b6de-738554e1b0fa"
alarmchannel = "5fbc8e9f-2fc7-48a3-99bc-d8f5e74e7854"

datatopic="channels/" + datachannel +  "/messages"
alarmtopic="channels/" + alarmchannel +  "/messages"


def on_connect(client, userdata, flags, rc):
 print("Connected with result code" + strc(rc))

client = mqtt.Client()
client.on_connect= on_connect
client.username_pw_set(thing_id,thing_key)    #set username and password
client.connect(broker_address,broker_port)
client.loop_start()
while True:
    temp = random.randint(21,24)
    print (temp)
    time.sleep(2)
    client.publish(datatopic, payload = "[{\"n\":\"temperature\",\"u\":\"Cel\",\"v\":" + str(temp) + "}]")
    if temp > 22  :
      client.publish(alarmtopic, payload = "red")
    else :
      client.publish(alarmtopic, payload = "green")
