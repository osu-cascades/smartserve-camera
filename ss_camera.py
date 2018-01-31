import picamera

def take_pic():
	camera = picamera.PiCamera()
	
	camera.capture('image.jpg')


