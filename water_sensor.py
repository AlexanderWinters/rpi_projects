from machine import I2C, Pin
import time

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Constants
NO_TOUCH = 0xFE
THRESHOLD = 100
ATTINY1_HIGH_ADDR = 0x78 
ATTINY2_LOW_ADDR = 0x77

# Data buffers
low_data = bytearray(8)
high_data = bytearray(12)

def get_high12_section_value():
    global high_data
    high_data = bytearray(i2c.readfrom(ATTINY1_HIGH_ADDR, 12))
    time.sleep(0.01)

def get_low8_section_value():
    global low_data
    low_data = bytearray(i2c.readfrom(ATTINY2_LOW_ADDR, 8))
    time.sleep(0.01)

def check():
    sensorvalue_min = 250
    sensorvalue_max = 255
    low_count = 0
    high_count = 0
    
    while True:
        touch_val = 0
        trig_section = 0
        low_count = 0
        high_count = 0
        
        get_low8_section_value()
        get_high12_section_value()
        
        print("low 8 sections value = ")
        for i in range(8):
            print(low_data[i], end=".")
            if sensorvalue_min <= low_data[i] <= sensorvalue_max:
                low_count += 1
            if low_count == 8:
                print("      PASS")
        print("  ")
        print("  ")
        
        print("high 12 sections value = ")
        for i in range(12):
            print(high_data[i], end=".")
            if sensorvalue_min <= high_data[i] <= sensorvalue_max:
                high_count += 1
            if high_count == 12:
                print("      PASS")
        print("  ")
        print("  ")
        
        for i in range(8):
            if low_data[i] > THRESHOLD:
                touch_val |= 1 << i
        
        for i in range(12):
            if high_data[i] > THRESHOLD:
                touch_val |= 1 << (8 + i)
        
        while touch_val & 0x01:
            trig_section += 1
            touch_val >>= 1
        
        print("water level = ", trig_section * 5, "% ")
        print(" ")
        print("*********************************************************")
        time.sleep(1)

# Main function
def main():
    check()

if __name__ == "__main__":
    main()
