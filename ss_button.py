import RPi.GPIO as GPIO
import time
import ss_camera

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	button_state = GPIO.input(24)
	if button_state == False:
		ss_camera.take_pic()
		time.sleep(.2)
