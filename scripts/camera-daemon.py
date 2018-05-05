from camera import Camera
from gpiozero import Button
from signal import pause
from database import insert

button = Button(17)
camera = Camera()

def capture():
	camera.capture_image(False)

button.when_pressed = capture

print("running...")

pause()




