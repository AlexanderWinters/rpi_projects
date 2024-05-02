import utime
import asyncio
from machine import Pin

controller = Pin(19, Pin.OUT)
yellow_led = Pin(2, Pin.OUT)
red_led = Pin(4, Pin.OUT)
green_led = Pin(6, Pin.OUT)
breaker = Pin(22, Pin.IN, Pin.PULL_DOWN)

green_button = Pin(21, Pin.IN, Pin.PULL_DOWN)
yellow_button = Pin(10, Pin.IN, Pin.PULL_DOWN)
red_button = Pin(12, Pin.IN, Pin.PULL_DOWN)

def clean():
    for x in range(3):
        controller.high()
        utime.sleep(.2)
        controller.low()
    yellow_led.low()
    red_led.low()
    green_led.low()

def start_check():
    for x in range(3):
        controller.high()
        yellow_led.high()
        red_led.high()
        green_led.high()
        utime.sleep(.2)
        controller.low()
        yellow_led.low()
        red_led.low()
        green_led.low()
        utime.sleep(.2)

def button_tester():
    while True:
        stopper = False
        if (green_button.value()):
            green_led.high()
            utime.sleep(.1)
            green_led.low()
        if (yellow_button.value()):
            yellow_led.high()
            utime.sleep(.1)
            yellow_led.low()
        if (red_button.value()):
            red_led.high()
            utime.sleep(.1)
            red_led.low()
        if (breaker.value()):
            controller.high()
            utime.sleep(.5)
            controller.low()
            break;


start_check()
button_tester()
clean()

