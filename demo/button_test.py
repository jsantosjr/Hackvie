import RPi.GPIO as GPIO
import time
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)

led_pin = 26
button_pin = 19

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Your Account SID from twilio.com/console
account_sid = "AC5beb685ec9f3ed7943ec95e46d5f1e99"
# Your Auth Token from twilio.com/console
auth_token  = "0b7eac8a2c8d659b379b9d259467d08a"


try:
	while True:
		input_state = GPIO.input(19)
		if input_state == False:
#			GPIO.output(led_pin, True)
			break

        client = Client(account_sid, auth_token)
#        x = 113
#        x = str(x)
        message = client.messages.create(
            to="+15104568405", 
            from_="+16692226247",
#            body="Heart Rate: " + x + " BPM")
            body="The button was pressed")
            
#			i+=1
#			print('Button Pressed {} times'.format(i))
#			continue
#		else:
#			GPIO.output(led_pin, False)
#		
#		time.sleep(0.5)


finally:
	print("Cleaning up")
	GPIO.cleanup()
