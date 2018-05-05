from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime
from signal import pause

button = Button(17)
camera = PiCamera()
camera.resolution = (400,400)

def capture():
	filename = datetime.now().isoformat()
	camera.start_preview()
	print("say cheese...!")
	sleep(1)
	print("3...")
	sleep(1)
	print(".2..")
	sleep(1)
	print("..1.")
	sleep(1)
	camera.stop_preview()
	# allow time for camera to warm up and focus
	camera.capture('./captures/%s.jpg' % filename)

button.when_pressed = capture

print("running...")
pause()




