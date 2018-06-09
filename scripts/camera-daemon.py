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

def capture():
    return capture_stream(True)

def prepare_camera(preview):
        # if preview is passed we want to use the preview
        if preview:
            camera.start_preview()

        # these print statements help for debugging as well as
        # allowing time for the camera to warm up
        print("taking picture in")
        print("5")
        sleep(1)
        print("4")
        sleep(1)
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


def main():
    picture_count = 0
    print("picture count ", picture_count)
    while True:
        global picture_count
        print("running...")
        # wait for the first picture
        button.wait_for_press(timeout=None)
        # take the irst picture after button pressed
        image1 = capture()
        print("picture count ", picture_count)
        # increment picture count
        picture_count = picture_count + 1
        print("Waiting for second picture")
        # wait for second picture
        button.wait_for_press(timeout=None)
        # take the second image
        image2 = capture()
        print("picture count ", picture_count)
        # increment picture count
        picture_count = picture_count + 1
        # when two pictures have been taken, compute the difference 
        if(picture_count == 2):
            # reset the picture count
            picture_count = 0
            # compute the difference
            diff = compute_diff(image1, image2)
            # insert the difference into the database
            insert(diff)
            print("Structural difference: %s %%" % (diff*100))
            
if __name__== "__main__":
    main()
