from machine import Pin
import utime

red = Pin(8, Pin.OUT)
laser = Pin(1, Pin.OUT)
green = Pin(4, Pin.OUT)

laser.low()
#switch.irq(lambda pin: print("IRQ with flags:", pin.irq().flags()), Pin.IRQ_FALLING)
