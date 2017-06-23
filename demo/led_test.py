import RPi.GPIO as GPIO
import time
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)

led_pin = 26

GPIO.setup(led_pin, GPIO.OUT)

try:
        # The long led prong should be in line with the power wire.
	while True:
                GPIO.output(led_pin, False)
                time.sleep(0.8)
                GPIO.output(led_pin, True)
                time.sleep(0.2)


finally:
	print("Cleaning up")
	GPIO.cleanup()
