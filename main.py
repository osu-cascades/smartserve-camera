import RPi.GPIO as GPIO
import time
import picamera
import datetime

# Save photo as YYYYMMDDHHmmss.jpg.
def take_pic():
    now = datetime.datetime.now()
    img_name = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '.jpg'
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    camera = picamera.PiCamera()
    camera.capture(img_name)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	button_state = GPIO.input(24)
	if button_state == False:
		take_pic()
		time.sleep(.2)
