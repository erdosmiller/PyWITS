import sys
import getopt
import serial
from PyWITS import Globals
from PyWITS.Receiver import Receiver

optlist, args = getopt.getopt(sys.argv[1:], '', ['baud=','timeout='])

baud = 9600
timeout = 0.5

try:
    device = args[0]
except IndexError:
    raise ValueError('Device must be specified!')

for opt in optlist:
    if opt[0] == '--baud':
        baud = int(opt[1])

ser = serial.Serial(device,baud,timeout=timeout)
rec = Receiver(ser)

import time

data = rec.ask(Globals.DATA_REQUEST)

print data
for d in data:
    print d,'-',

