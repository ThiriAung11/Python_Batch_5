from signal import pause

num = 0
action = str(input())

while action == " ":
    num += 1

if num/2 == 0:
    print("LED is off")
else:
    print("LED is on")

pause()
