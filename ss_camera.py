import picamera
import datetime

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
img_name = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '.jpg'

#image name is time stamp that reads year month day hour minute second
def take_pic():
	camera = picamera.PiCamera()
	camera.capture(img_name)


