from picamera import PiCamera
from gpiozero import Button
from signal import pause
from time import sleep
from database import insert
from skimage.measure import compare_ssim as ssim
import numpy as np
import cv2

button = Button(17)
camera = PiCamera()
camera.resolution = (416,400)

def capture(image=null):
    # create flag to track second button click
    secondClick = False
    # take the first image
    image1 = capture_stream(True)

    while secondClick == False:
        # pauses the script until button is pressed again
        button.wait_for_press(timeout=None)
        secondClick = True
        
    # take second picture and compute
    image2 = capture_stream(True)
    diff = compute_diff(image1, image2)
    insert(diff)


def prepare_camera(preview):
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
        # create empty numpy array to match capture size
        image = np.empty((400, 416, 3), dtype=np.uint8)
        prepare_camera(preview)
        # save the image to the numpy array
        camera.capture(image, 'bgr')
        return image

# compute image diffs based on structural similarity
def compute_diff(A, B):
    imageA = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)
    return ssim(imageA, imageB)


button.when_pressed = capture

print("running...")

pause()




