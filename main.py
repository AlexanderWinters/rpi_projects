import time
import board
import busio
import adafruit_lsm6ds
import hid
device = hid.device()
device.open(0xCAFE, 0x4005)

i2c = busio.I2C(board.SCL, board.SDA)
sox = adafruit_lsm6ds(i2c)

print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (device.acceleration))
print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s" % (device.gyro))

device.close()
