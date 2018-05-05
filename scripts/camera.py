from picamera import PiCamera
from datetime import datetime
from time import sleep
from io import BytesIO
from PIL import Image


class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.resolution = (400, 400)

    def prepare_camera(self, preview):
        # if preview is passed we want to use the preview
        if preview:
            self.camera.start_preview()

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
            self.camera.stop_preview()


    def capture_image(self, preview):
        filename = datetime.now().isoformat() + ".jpg"

        self.prepare_camera(preview)

        # save the image and return the filename just in case we
        # want to fetch the same file later
        self.camera.capture("/home/pi/smartserve/smartserve-camera/captures/%s" % filename)
        return filename

    def capture_stream(self, preview):
        stream = BytesIO()

        self.prepare_camera(preview)
        
        # save the image to the stream and return it
        self.camera.capture(stream, format='jpeg')
        # rewind the stream so we can read its contents
        stream.seek(0)
        return Image.open(stream)
        
