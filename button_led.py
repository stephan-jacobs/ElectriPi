import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

print("started running")

count = 0

while True:
    if GPIO.input(19) == GPIO.HIGH:
        pushed = True
        count += 1
        print("Button was pushed! ({} times)".format(count))
        while pushed:
            time.sleep(0.1)
            if GPIO.input(19) == GPIO.LOW:
                pushed = False
        if count % 2 == 1:
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)