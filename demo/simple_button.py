import RPi.GPIO as GPIO
import time
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)

button_pin = 19

print("Setting up GPIO")
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
        print("Listening for button")
	while True:
		input_state = GPIO.input(19)
		if input_state == False:
                        print("Button pressed.")
                        time.sleep(0.2)
			break


finally:
	print("Cleaning up")
	GPIO.cleanup()
