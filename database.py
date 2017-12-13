#!/usr/bin/env python
#Bovenste regel maakt de file executable

import time
import datetime
import glob
import MySQLdb
import RPi.GPIO as GPIO #RPi.GPIO wordt nu GPIO genoemd
from time import strftime

InputPin = 18
voltage = 0
current = 0

#Variabelen voor MySQL
db = MySQLdb.connect(host="localhost", user="root", passwd="Mobility", db="Windturbine_database")
cur = db.cursor()

GPIO.setmode(GPIO.BCM)

GPIO.setup(InputPin, GPIO.IN)

if GPIO.input(InputPin) == True:
	voltage = 5

else:
	voltage = 0

while True:
	datetimeWrite = (time.strftime("%Y-%m-%d") + time.strftime(" %H:%M:%S"))
	print voltage
	print current
	print datetimeWrite
	sql = ("""INSERT INTO WindturbineLog (datetime, Voltage, Current) VALUES (%s,%s, %s)""",(datetimeWrite, voltage, current))
	try:
		print "Writing to database..."
		cur.execute(*sql)
		db.commit()
		print "Write Complete"

	except:
		db.rollback()
		print "Failed writing to database"

	cur.close()
	db.close()
	break
