import string, re

import globals

from packet import Identifier, DataRecord, LogicalRecord

class IO(object):
    def write(self, data):
        "writes a string out"
        raise NotImplementedError, "subclasses of IO must implement this method"
    def read(self):
        "reads a string in"
        raise NotImplementedError, "subclasses of IO must implement this method"

class SerialIO(IO):
    def __init__(self, serial):
        self.serial = serial

    def write(self, data):
        self.serial.write(data)

    def read(self, data):
        data = []
        new_data = None
        while(new_data != ''):
            new_data = self.io.read()
            data.append(new_data)
        return ''.join(data)

class WITS0Communicator(object):
    def __init__(self, io):
        self.io = io
        
    def write(self,data):
        self.io.write(data)

    def ask(self,question):
        self.write(question)
        return self.read()

    def read(self):
        return self._unpack_data(self.io.read())

    def _unpack_data(self,data):
        set_re = re.compile(globals.LOGICAL_RECORD_BEGIN + '[^&^!]*' + 
                            globals.LOGICAL_RECORD_END,re.DOTALL) 

        logical_record_strings = set_re.findall(data)
        return [self._unpack_logical_record(x)
                for _,x in enumerate(logical_record_strings)]

    def _unpack_logical_record(self, logical_record_string):
        begin_length = len(globals.LOGICAL_RECORD_BEGIN)
        end_length = len(globals.LOGICAL_RECORD_END)
        stripped_logical_record = logical_record_string[begin_length:-end_length]
        data_record_strings = stripped_logical_record.split(globals.DATA_ITEM_SEPERATOR)
        data_records = [self._unpack_data_record(x) 
                        for x in data_record_strings if x != '']
        return LogicalRecord(data_records)
        

    def _unpack_data_record(self, data_record_string):
        record_identifier = data_record_string[0:2]
        item_identifier = data_record_string[2:4]
        value = data_record_string[4:]
        ident = Identifier(record_identifier,item_identifier)
        return DataRecord(ident,value)

if __name__ == '__main__':
    
    test_str = '&&\r\n1984PASON/EDR\r\n0108519.48\r\n01103705.81\r\n01130.00\r\n01230.00\r\n01240.00\r\n01250.00\r\n0137987626.00\r\n01426229.27\r\n0143495787.00\r\n0144491839.00\r\n01450.00\r\n!!\r\n'
    
    print WITS0Communicator(None)._unpack_data(test_str)
