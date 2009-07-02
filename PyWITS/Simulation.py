import sys
import getopt
import serial
import time

from PyWITS.Transmitter import Transmitter
from PyWITS.Receiver import Receiver
from PyWITS.Objects.Identifier import Identifier
from PyWITS.Objects.DataItem import DataItem
from PyWITS.Objects.DataRecord import DataRecord

optlist, args = getopt.getopt(sys.argv[1:], '', ['baud=','timeout='])

baud = 9600
timeout = 0.25

try:
    device = args[0]
except IndexError:
    raise ValueError('Device must be specified!')

for opt in optlist:
    if opt[0] == '--baud':
        baud = int(opt[1])

ser = serial.Serial(device,baud,timeout=timeout)

trans = Transmitter(ser)
rec = Receiver(ser)

#gamma ray
inclination_identifier = Identifier(record_identifier='07',item_identifier='13')
inclination_data_item = DataItem(identifier=inclination_identifier,value='00.0')

azimuth_identifier = Identifier(record_identifier='07',item_identifier='15')
azimuth_data_item = DataItem(identifier=azimuth_identifier,value='00.0')

gamma_ray_identifier = Identifier(record_identifier='08',item_identifier='21')
gamma_ray_data_item = DataItem(identifier=gamma_ray_identifier,value='00.0')

#tvd_identifier = Identifier(record_identifier='01',item_identifier='08')
#tvd_data_item = DataItem(identifier=tvd_identifier,value='00.0')

#bit depth
bit_depth_identifier = Identifier(record_identifier='01',item_identifier='08')
bit_depth_data_item = DataItem(identifier=bit_depth_identifier,value='00.0')

#hole depth
hole_depth_identifier = Identifier(record_identifier='01',item_identifier='10')
hole_depth_data_item = DataItem(identifier=hole_depth_identifier,value='00.0')

#rop
rop_identifier = Identifier(record_identifier='01',item_identifier='13')
rop_data_item = DataItem(identifier=rop_identifier,value='00.0')


test_data_record = DataRecord(data_items=[inclination_data_item,azimuth_data_item])

test_data_record2 = DataRecord([gamma_ray_data_item])

test_data_record3 = DataRecord([bit_depth_data_item,hole_depth_data_item,rop_data_item])

x = 0
count1 = 738.21
count2 = 1128.21
count3 = 143.21

try:
    while(1):
        #print '%04.1f' % x
        inclination_data_item.value = '%04.1i' % x
        azimuth_data_item.value = '%04.1i' % (2*x)
        gamma_ray_data_item.value = '%04.1i' % (3*x)
        bit_depth_data_item.value = '%05.2f' % (count1+x)
        hole_depth_data_item.value = '%05.2f' % (count2+x)
        rop_data_item.value = '%05.2f' % (count3+x)
        
        

        x += 1
        print "Writing"
        trans.write(test_data_record)
        trans.write(test_data_record2)
        trans.write(test_data_record3)
        #print "Reading"
        #rec.read()
        time.sleep(1)
        
except KeyboardInterrupt:
    pass
