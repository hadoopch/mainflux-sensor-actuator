#!/usr/bin/env python3

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#PINs
PIN_RED=17
PIN_GREEN=27

GPIO.setup(PIN_RED,GPIO.OUT)
GPIO.setup(PIN_GREEN,GPIO.OUT)

broker_address = "53.252.161.120"
broker_port=1884
#Led
thing_id = "48ceccff-1140-44cc-8522-a1890ab42958"
thing_key = "028606bf-96fb-4485-a70b-f9ea726599dc"

#actionchannel
alarmchannel = "5fbc8e9f-2fc7-48a3-99bc-d8f5e74e7854"
alarmtopic="channels/" + alarmchannel +  "/messages"


def on_connect(client, userdata, flags, rc):
  print("Connected with result code" + str(rc))
  client.subscribe(alarmtopic)

def on_message(client, userdata, msg):
    value=str(msg.payload.decode('UTF-8'))
    if "red" in value :
        print("Temperature is too high")
        GPIO.output(PIN_RED,GPIO.HIGH)
        GPIO.output(PIN_GREEN,GPIO.LOW)
    elif "green" in value :
        print("Temperature is OK")
        GPIO.output(PIN_RED,GPIO.LOW)
        GPIO.output(PIN_GREEN,GPIO.HIGH)
    else :
        print( "Unknown message")

client = mqtt.Client()
client.username_pw_set(thing_id,thing_key)
client.on_connect= on_connect
client.on_message= on_message
client.connect(broker_address,broker_port)
client.loop_forever()

