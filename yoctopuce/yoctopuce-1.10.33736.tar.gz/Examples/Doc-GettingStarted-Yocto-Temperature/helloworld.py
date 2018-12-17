# ********************************************************************
#
#  $Id: helloworld.py 32630 2018-10-10 14:11:07Z seb $
#
#  An example that show how to use a  Yocto-Temperature
#
#  You can find more information on our web site:
#   Yocto-Temperature documentation:
#      https://www.yoctopuce.com/EN/products/yocto-temperature/doc.html
#   Python API Reference:
#      https://www.yoctopuce.com/EN/doc/reference/yoctolib-python-EN.html
#
# *********************************************************************

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
# add ../../Sources to the PYTHONPATH
sys.path.append(os.path.join("..", "..", "Sources"))

from yoctopuce.yocto_api import *
from yoctopuce.yocto_temperature import *


def usage():
    scriptname = os.path.basename(sys.argv[0])
    print("Usage:")
    print(scriptname + ' <serial_number>')
    print(scriptname + ' <logical_name>')
    print(scriptname + ' any  ')
    sys.exit()


def die(msg):
    sys.exit(msg + ' (check USB cable)')


errmsg = YRefParam()

if len(sys.argv) < 2:
    usage()

target = sys.argv[1]

# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
    sys.exit("init error" + errmsg.value)

if target == 'any':
    # retreive any temperature sensor
    sensor = YTemperature.FirstTemperature()
    if sensor is None:
        die('No module connected')
else:
    sensor = YTemperature.FindTemperature(target + '.temperature')

if not (sensor.isOnline()):
    die('device not connected')

while sensor.isOnline():
    print("Temp :  " + "%2.1f" % sensor.get_currentValue() + "°C (Ctrl-C to stop)")
    YAPI.Sleep(1000)
YAPI.FreeAPI()
