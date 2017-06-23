import RPi.GPIO as GPIO
import time
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)

led_pin = 26
button_pin = 19

print("Setting up GPIO")
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Your Account SID from twilio.com/console
#account_sid = "AC5beb685ec9f3ed7943ec95e46d5f1e99"
# Your Auth Token from twilio.com/console
#auth_token  = "0b7eac8a2c8d659b379b9d259467d08a"


try:
        print("Listening for button")
	while True:
		input_state = GPIO.input(19)
		if input_state == False:
                        print("Button pressed -- check light.")
			GPIO.output(led_pin, False)
			time.sleep(0.2)
		else:
                        GPIO.output(led_pin, True)


##	print("Turning light off.")
##        GPIO.output(led_pin, False)
##        time.sleep(2.0)
##	print("Sending text.")
##        client = Client(account_sid, auth_token)
##        message = client.messages.create(
##        to="+15104568405", 
##        from_="+16692226247",
##        body="The button was pressed")



finally:
	print("Cleaning up")
	GPIO.cleanup()
