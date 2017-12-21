#!/usr/bin/env python
#Bovenste regel maakt de file executable

import time
import datetime
import glob
import MySQLdb
import Adafruit_ADS1x15
import RPi.GPIO as GPIO #RPi.GPIO wordt nu GPIO genoemd
from time import strftime

#Create an ADS1115 ADC(16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

#Set the I2C adress
adc = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)

InputPin = 18
voltage = 5.32
current = 1.65
GAIN = 1

#Variabelen voor MySQL
db = MySQLdb.connect(host="localhost", user="root", passwd="Mobility", db="Windturbine_database")
cur = db.cursor()

GPIO.setmode(GPIO.BCM)
GPIO.setup(InputPin, GPIO.IN)

voltage = adc.read_adc(0, gain=GAIN)
current = adc.read_adc(1, gain=GAIN)

while True:
	voltage = float(voltage)
	current = float(current)
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
