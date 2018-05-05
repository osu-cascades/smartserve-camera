import sqlite3
import traceback
from datetime import datetime

def insert(diff, rfid=''):
	# connect to our sqlite database
	conn = sqlite3.connect('/home/pi/smartserve/smartserve.db')
	cursor = conn.cursor()

	# create the timestamp
	measured_on = datetime.now().isoformat()	
	
	# try to insert the data, catch the exception if it doesn't work
	try:
		cursor.execute("INSERT INTO plates (rfid, difference, measured_on) VALUES ({rfid}, {diff}, {time});".format(rfid=rfid, diff=diff, time=measured_on))
	except Exception, err:
		print("Something went wrong while inserting data.") 
		traceback.print_exc()

	# commit the insert statement and close the connection
	conn.commit()
	conn.close()
