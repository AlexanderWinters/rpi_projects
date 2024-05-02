#11 leds strobing
#5 leds for the shooting mechanic
from machine import Pin
import utime
import random

ledlist = []
for x in range(1,6,1):
    ledname='LED' + str(x)
    ledname=Pin(x,Pin.OUT)
    ledlist.append(ledname)

button = Pin(20, Pin.IN, Pin.PULL_DOWN)
def clean():
    for led in ledlist:
        led.low()

#I can create my own Δt by stamping the time the script started and subtracting the time now. Δt is measure in seconds.
while True:
    startTimer = utime.time()
    if (button.value()):
        for led in ledlist:
            led.high()
            utime.sleep(.03)
            led.low()
        while (button.value()):
            deltaTime = abs(startTimer-utime.time())
            print(deltaTime)
        
        utime.sleep(.1)

clean()