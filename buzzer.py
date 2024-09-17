import time
from machine import Pin
Buzzer = Pin(6, Pin.OUT)
while 1:
    #bomb sound
    Buzzer.toggle()
    time.sleep(0.5)

    

    


