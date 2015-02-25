from __future__ import absolute_import
from django.shortcuts import render
from celery import shared_task 
import time
import measure.SCPI as SCPI
import json


@shared_task
def current_measure(obj):
    device = SCPI.SCPI("192.168.0.94")
    if (obj.voltage > 3.8):
        raise Exception('Voltage too high') 

    device.setVoltage(1, obj.voltage)
    device.setOutput(1,True)
    device.startCurrentMeasurement(1, obj.resolution*obj.time, obj.resolution)
    time.sleep(obj.time*2)
    current = device.getCurrentMeasurements(1,obj.resolution*obj.time)
    device.setOutput(1,False)

    obj.measure_list = json.dumps(current)
    avg = sum(current)/float(len(current))
    obj.average = avg
    obj.save()
