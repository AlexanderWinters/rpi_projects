from machine import Pin
import utime

ledlist = []
for x in range (1, 10, 1):
    ledname = 'LED' + str(x)
    ledname = Pin(x, Pin.OUT)
    ledlist.append(ledname)

button = Pin(20, Pin.IN, Pin.PULL_DOWN)

def clean ():
    for led in ledlist:
        led.low()

def test_all ():
    for led in ledlist:
        led.high()
        utime.sleep(.05)
        led.low()

i = 0
s = 1
speed = .05
while True:
    if i == 0:
        s = 1
    elif i == 8:
        s = -1
    ledlist[i].high()
    utime.sleep(speed)
    ledlist[i].low()
    i += s
    

test_all()
clea()