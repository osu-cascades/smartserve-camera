from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

button = Button(17)
camera = PiCamera()

def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)

button.when_pressed = capture

pause()
