import RPi.GPIO as GPIO
import time
from twilio.rest import Client
from Adafruit_BME280 import *

def sendSms(client, message):
	print("Sending text.")
	message = client.messages.create(
        to="+15104568405", 
        from_="+16692226247",
        body=message)
	

GPIO.setmode(GPIO.BCM)

led_pin = 26
button_pin = 19

print("Setting up GPIO")
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
degreesF = (sensor.read_temperature() * 1.8) + 32

# Your Account SID from twilio.com/console
account_sid = "AC5beb685ec9f3ed7943ec95e46d5f1e99"

# Your Auth Token from twilio.com/console
auth_token  = "0b7eac8a2c8d659b379b9d259467d08a"
client = Client(account_sid, auth_token)
sleepDuration = 0.2
location = "https://www.google.com/maps/place/Atkins+Bldg,+1801+S+1st+St,+Champaign,+IL+61820/@40.094094,-88.2383216,16z/data=!4m2!3m1!1s0x880cd7290ec441e5:0x36528d0ebcec9622"

try:
	print("Listening for button")
	while True:
		input_state = GPIO.input(19)
		if input_state == False:
			print("Button pressed -- check light.")
			degreesF = (sensor.read_temperature() * 1.8) + 32
			degreesAsString = "{0:0.3f}".format(degreesF)
			print 'Temp      = {} deg F'.format(degreesAsString)
			
			sleepDuration = 0.2
			if degreesF > 40:
				sendSms(client, "Omar's Temp is {} degrees.\nHis location is {}".format(degreesAsString, location))
				GPIO.output(led_pin, False)
				
			time.sleep(sleepDuration)
		else:
			GPIO.output(led_pin, True)
				
				# The temperature is too high so we'll perform a callout to the Twilio API.
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
