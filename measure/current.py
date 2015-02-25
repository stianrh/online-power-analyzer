#!/usr/bin/python
import SCPI
import time
from pylab import *
from types import *
from numpy import array

def start_measure():
	# open remote measurement device (replace "hostname" by its actual name)
	device = SCPI.SCPI("192.168.0.94")


	#setup voltage meter
	device.setVoltage(1, 2.8) 
	#device.setCurrent(1, 0.1)

	# enable output
	device.setOutput(1,True)


	print "Start measurement..."
	device.startPowerMeasurement(1, 3000);

	time.sleep(10)
	print "Collect data..."
	current = device.getCurrentMeasurements(1, 30000)

	time = 0

	# plot data
	for item in current:
		print str(time) + " " + str(item) + "\n"
		time = time + 0.001


