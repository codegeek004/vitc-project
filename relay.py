import time
from machine import Pin
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
relay = Pin(7, Pin.OUT)
for x in range(5):
    relay.value(1)
    led2.value(1)
    led3.value(0)
    time.sleep(1)
    relay.value(0)
    led2.value(0)
    led3.value(1)
    time.sleep(1)
    led3.value(0)
    print(x, "LEDs toggled successfully")
    

