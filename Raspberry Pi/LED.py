from gpiozero import LED
from time import sleep

# Create an object called led that refers to GPIO 12
led = LED(12)

# Create variable called delay that refers to delay time in seconds
delay = 1

while True:
    # set led to on for delay time
    led.on()
    print('LED set to on')
    sleep(delay)
    # set led to off for delay time
    led.off()
    print('LED set to off')
    sleep(delay)
