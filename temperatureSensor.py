import time
from machine import Pin
conversion_factor = 3.3/(65536)
adc2 = machine.ADC(27)
while(1):
    adcvalue = adc2.read_u16()
    temp = int((adcvalue * conversion_factor)*100)
    print("temperature", temp, "C")
    time.sleep(1)
    


