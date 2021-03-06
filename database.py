#!/usr/bin/env python
#Bovenste regel maakt de file executable

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
import datetime
import glob
import MySQLdb
import Adafruit_ADS1x15
import RPi.GPIO as GPIO #RPi.GPIO wordt nu GPIO genoemd
from time import strftime

#Create an ADS1115 ADC(16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

#Set the I2C adress, ADDR -> VDD
adc = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)

InputPin = 18
voltage = 5.32
current = 1.65
GAIN = 2 #gain = 2 for measure of voltage +/- 2.048 
x = [i for i in range(0, 100, 1)]
voltages = []

#Variabelen voor MySQL
db = MySQLdb.connect(host="localhost", user="root", passwd="Mobility", db="Windturbine_database")
cur = db.cursor()

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(InputPin, GPIO.IN)

#voltage = adc.read_adc(0, gain=GAIN)
#current = adc.read_adc(1, gain=GAIN)

#adc.start_adc(0, gain=GAIN)

while True:
	voltage = float(voltage)
	current = float(current)
	datetimeWrite = (time.strftime("%Y-%m-%d") + time.strftime(" %H:%M:%S"))
	print voltage,;print'V' 
	print current,;print'A' 
	power = voltage * current
	print power,;print'W' 
	print datetimeWrite

	
#	start = time.time()
#	while (time.time() - start) <= 0.02:
#		value = adc.get_last_result()
#		print ('Channel 0: {0}' .format(value))
#	adc.stop_adc()

#F = 50Hz so T = 1/50 = 0.02S 
#I want 100 points to measure so I will make the delay 0.02S / 100 = 0.0002 S 
#	for i in range(0, 100, 1):
#		adcValueVoltage = adc.read_adc(0, gain=GAIN)
#		print adcValueVoltage
#		voltage =((adcValueVoltage/32767.0) * 2.048)
#		voltages.append(voltage)
#		print round(voltage,4)
		#time.sleep(0.0002) #sleep for 200uS

#	plt.scatter(x, voltages)
#	plt.savefig('Graph.png')
#	print 'Saved'

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
