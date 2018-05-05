from camera import Camera
from gpiozero import Button
from signal import pause
from time import sleep
from database import insert
from ssim import compute_diff

button = Button(17)
camera = Camera()

def capture():
	image1 = camera.capture_stream(False)
	sleep(3)
	image2 = camera.capture_stream(False)
	diff = compute_diff(image1, image2)
	print(diff)

button.when_pressed = capture

print("running...")

pause()




