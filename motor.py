from machine import Pin
import utime

motor = Pin(22, Pin.OUT)

motor.high()
utime.sleep(1)
motor.low()