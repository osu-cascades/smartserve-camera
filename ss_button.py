import RPi.GPIO as GPIO
import time
import ss_camera

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)

try:
	while True:
		button_state = GPIO.input(23)
		if button_state == False:
			GPIO.output(24, True)
			ss_camera.take_pic()
			time.sleep(2.0)
		else:
			GPIO.output(24, False)
except:
	GPIO.cleanup()
