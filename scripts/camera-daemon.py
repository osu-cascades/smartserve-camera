from picamera import PiCamera
from io import BytesIO
from PIL import Image
from gpiozero import Button
from signal import pause
from time import sleep
from database import insert
from skimage.measure import structural_similarity as ssim
import cv2

button = Button(17)
camera = PiCamera()
camera.resolution = (400,400)

def capture():
	image1 = capture_stream(False)
	sleep(3)
	image2 = capture_stream(False)
	diff = compute_diff(image1, image2)
	print(diff)


def prepare_camera(preview):
        global camera
        # if preview is passed we want to use the preview
        if preview:
            camera.start_preview()

        # these print statements help for debugging as well as
        # allowing time for the camera to warm up
        print("taking picture in")
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)

        # stop the camera's preview
        if preview:
            camera.stop_preview()

def capture_stream(preview):
        global camera
        stream = BytesIO()

        prepare_camera(preview)
        
        # save the image to the stream and return it
        camera.capture(stream, format='jpeg')
        # rewind the stream so we can read its contents
        stream.seek(0)
        return Image.open(stream)

# compute image diffs based on structural similarity
def compute_diff(A, B):
    imageA = cv2.imread(A)
    imageB = cv2.imread(B)

    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    return ssim(imageA, imageB)


button.when_pressed = capture

print("running...")

pause()




