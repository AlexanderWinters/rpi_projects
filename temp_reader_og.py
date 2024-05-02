import machine
import utime

sensor=machine.ADC(4)
factor = 3.3/65535

while True:
    reading = sensor.read_u16() * factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(round(temperature, 2))
    utime.sleep(2)