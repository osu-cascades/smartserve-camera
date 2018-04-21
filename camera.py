from picamera import PiCamera
import time
import requests

def main():
    url = "http://localhost:3000/upload"
    filename = get_snapshot()
    files = { 'media', open(filename, 'rb') }
    requests.post(url, files)


def get_snapshot():
    camera = PiCamera()
    camera.resolution = (1024,768)

    filename = time.strftime("%Y%m%d-%H%M%S")
    filename = filename + ".jpg"

    camera.start_preview()
    # allow camera to warm up
    time.sleep(2)
    camera.capture(filename)
    return filename