from machine import Pin
import utime

red = Pin(8, Pin.OUT)
green = Pin(4, Pin.OUT)

switch = Pin(20, Pin.IN, Pin.PULL_DOWN)

red.high()
green.low()

#switch.irq(lambda pin: print("IRQ with flags:", pin.irq().flags()), Pin.IRQ_FALLING)

while True: 
    if (switch.value()):
        red.toggle()
        green.toggle()
        utime.sleep(0.5)
        