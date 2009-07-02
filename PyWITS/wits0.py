import string, re

import globals

from packet import identifier, data_record, logical_record

def unpack_data(data):
    set_re = re.compile(globals.LOGICAL_RECORD_BEGIN + '[^&^!]*' + globals.LOGICAL_RECORD_END,re.DOTALL) 
    
    #after we call the re the data should be split up into raw data records
    logical_records = set_re.findall(data)

    #remove the headings
    unpacked_logical_records = []

    for i, lr in enumerate(logical_records):
        stripped_lr = lr[len(globals.LOGICAL_RECORD_BEGIN):0-len(globals.LOGICAL_RECORD_END)]
        
        data_records = []
        
        for dr in stripped_lr.split(globals.DATA_ITEM_SEPERATOR):
            if dr != '':
                r_ident = dr[0:2]
                d_ident = dr[2:4]
                d_value = dr[4:]
                
                ident = identifier(r_ident,d_ident)
                
                data_records.append(data_record(ident,d_value))

        unpacked_logical_records.append(logical_record(data_records))

    return unpacked_logical_records

class wits0:
    def __init__(self,device):
        """A base class for representing a WITS0 connection.
        The device is the serial interface.
        """
        
        self.device = device
        
    def write(self,data):
        """Send a data record"""
        self.device.write(data)

    def ask(self,question):
        self.device.write(question)
        return self.read()

    def read(self):
        data = []
        new_data = None

        while(new_data != ''):
            new_data = self.device.read()
            data.append(new_data)

        print "!!!",new_data

        return unpack_data(string.join(data,''))

if __name__ == '__main__':
    
    test_str = '&&\r\n1984PASON/EDR\r\n0108519.48\r\n01103705.81\r\n01130.00\r\n01230.00\r\n01240.00\r\n01250.00\r\n0137987626.00\r\n01426229.27\r\n0143495787.00\r\n0144491839.00\r\n01450.00\r\n!!\r\n'
    
    print unpack_data(test_str)
