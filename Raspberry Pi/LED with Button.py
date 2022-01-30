from gpiozero import LED, Button
from signal import pause

led = LED(12)
button = Button(23)

num = 0

while button.is_pressed():
    num += 1
    break

if num/2 == 0:
    print("Led is off")
else:
    print("Led is on")

pause()