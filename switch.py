import time
from machine import Pin
sw1 = Pin(5, Pin.IN)
led2 = Pin(2, Pin.OUT)
while(1):
    b1 = sw1.value()
    if b1 == 0:
        led2.value(1)
        print("Button pressed", not b1)
        
    else:
        led2.value(0)
        print("button not pressed")
    #another approach
    #led2.value(not b1)
    time.sleep(0.5)
    


