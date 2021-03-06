import time
import paho.mqtt.client as mqtt
import random
import os

mqttc=mqtt.Client()
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()

#read temperature
def read_sound_data():
    return random.randint(0, 500)

#publish temperature
while 1:
    t=read_sound_data()
    print "Publishing data"
    device_uuid=os.environ['RESIN_DEVICE_UUID'];
    print device_uuid
    (result,mid)=mqttc.publish("topic/GeneralizedIoT/"+str(device_uuid),t,2)
    time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()