import gpiozero
from time import sleep

relay1 = gpiozero.OutputDevice(26, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(20, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(21, active_high=False, initial_value=False)

relay1.on()
sleep (1)
relay1.off()