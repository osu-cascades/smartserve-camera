import RPi.GPIO as GPIO
import time

cautionLedPin = 2 # pin 2 is the yellow LED
readyLedPin = 3   # pin 3 is green LED
buttonPin = 18    # pin 18 == button
ledStatus = 1	# flag for led status

def setup():
	GPIO.setmode(GPIO.BCM)	# Numbers GPIOs by physical location
	GPIO.setup(cautionLedPin, GPIO.OUT)	# Set the yellow LED as output
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)	# set the buttons to input and the pull up to high
	GPIO.output(cautionLedPin, GPIO.HIGH)	# set the yellow led high to turn off

def switchLed(ev=None):
	global ledStatus	# get access to global variable
	ledStatus = not ledStatus
	GPIO.output(cautionLedPin, ledStatus)	# switch led status
	if ledStatus == 1:
		print 'LED off...'
	else:
		print '...LED on'

def loop():
	GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=switchLed, bouncetime=200) 	# wait for falling and set boune time to prevent led from being turned on then off again by accident
	while True:
		time.sleep(1)

def destroy():
	GPIO.output(cautionLedPin, GPIO.HIGH)	# led off
	GPIO.cleanup()	# release the bindings

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
