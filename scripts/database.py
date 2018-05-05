import sqlite3
import datetime

def insert(diff, rfid=''):
	# connect to our sqlite database
	conn = sqlite3.connect('/home/pi/smartserve/smartserve.db')
	cursor = conn.cursor()

	# create the timestamp
	measured_on = datetime.now().isoformat()	
	
	# try to insert the data, catch the exception if it doesn't work
	try:
		c.execute("INSERT INTO plates (rfid, difference, measured_on) VALUES ({rfid}, {diff}, {time});".format(rfid=rfid, diff=diff, time=measured_on))
	except:
		print("Something went wrong while inserting data.") 

	# commit the insert statement and close the connection
	conn.commit()
	conn.close()
