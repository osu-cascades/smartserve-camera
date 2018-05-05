import sqlite3
import traceback
from datetime import datetime

def insert(diff, rfid=''):
	# connect to our sqlite database
	conn = sqlite3.connect('/home/pi/smartserve/smartserve-camera/smartserve.db')
	cursor = conn.cursor()

	# create the timestamp
	measured_on = datetime.now().isoformat()	
	
	# try to insert the data, catch the exception if it doesn't work
	try:
		cursor.execute("INSERT INTO plates VALUES (?, ?, ?, ?);", (None, 'N/A', diff, measured_on))
	except Exception:
		print("Something went wrong while inserting data.") 
		traceback.print_exc()

	# commit the insert statement and close the connection
	conn.commit()
	conn.close()


def main():
        print("insterting...")
        insert(22.22)


if __name__ == '__main__':
        main()
