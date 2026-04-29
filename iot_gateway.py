# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:43:47 2026

@author: Nitin
"""

import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = '127.0.0.1'
PORT = 1883
TOPIC = 'factory/chemnitz/cnc_1/sensors'
STATUS_TOPIC = 'factory/chemnitz/cnc_1/state'

print("\n Building IIoT gateway")
client = mqtt.Client(client_id = 'CNC_1')
lwt_payload = json.dumps({'MACHINE':'CNC_1', 'STATUS':'FATAL ERROR'})
client.will_set(STATUS_TOPIC, payload = lwt_payload, qos=1, retain=True)
client.connect(BROKER,PORT)

client.loop_start()
online_payload = json.dumps({'MACHINE' : 'CNC_1', 'STATUS': 'ONLINE'})
client.publish(STATUS_TOPIC, payload = online_payload, qos=1, retain=True)


try:
    while True:
        machine_temp = round(random.uniform(75.0,110.0) , 2)
        machine_status =  "OVERHEATING" if machine_temp > 100  else "OK"
        payload = {
            "MACHINE" : "CNC_1",
            "MACHINE_TEMP" : machine_temp,
            "MACHINE_STATUS" : machine_status
            }
        json_envelope = json.dumps(payload)
        
        client.publish(TOPIC, json_envelope, qos=1)
        print(f"published:{json_envelope}")
        time.sleep(2)
        
        
except KeyboardInterrupt:
        print("\n shutting down gracefully...")
        
        offline_payload = json.dumps({'MACHINE':'CNC_1','STATUS':'GRACEFUL_SHUTDOWN'})
        client.publish(STATUS_TOPIC, payload = offline_payload, qos=1, retain=True)
        client.disconnect()
        client.loop_stop()
