import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
x = 0

while True:
    if GPIO.input(8) == GPIO.HIGH:
        x += 1
        print(f"Sensor was touched {x} times")
        sleep(.5)
