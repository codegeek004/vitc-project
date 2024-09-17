import time
from machine import Pin
adc2 = machine.ADC(28)
while(1):
    adcvalue = adc2.read_u16()
    print("ADC value(POT value)", adcvalue)
    time.sleep(1)
    

