import time
from machine import Pin
sw1 = Pin(5, Pin.IN)
sw2 = Pin(4, Pin.IN)
led3 = Pin(3, Pin.OUT)
led2 = Pin(2, Pin.OUT)
while(1):
    b1 = sw1.value()
    b2 = sw2.value()
    if b1 == 0:
        led2.value(1)
        print("Button1 pressed", not b1)
        
    else:
        led2.value(0)
        #print("button1 not pressed")
    #another approach
    #led2.value(not b1)
    time.sleep(0.5)
    if b2 == 0:
        led3.value(1)
        print("switch2 pressed")
    else:
        led3.value(0)
        #print("switch2 not pressed")
    time.sleep(0.5)
    


