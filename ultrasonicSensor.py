from time import sleep
from machine import Pin
from hcsr04 import HCSR04
import time
sensor = HCSR04(trigger_pin=15, echo_pin=14, echo_timeout_us=10000)
led2 = Pin(2, Pin.OUT)
while(1):
    distance = sensor.distance_cm()
    print("Distance: ", distance, ' cm')
    time.sleep(1)
    if distance < 15:
        led2.value(0)
        print("distance more than 15 cm")
    elif distance > 15:
        led2.value(1)
    else:
        led2.value(0)
        print("error")
    time.sleep(1)
        

