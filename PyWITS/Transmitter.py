from PyWITS.Objects.DataRecord import DataRecord
from PyWITS import Globals

class Transmitter:
    def __init__(self,device,mode=0):
        self.device = device
        self.mode = mode

    def write(self,data_record):

        if not isinstance(data_record,DataRecord):
            return ValueError('This is not valid data:',data_record)
        
        print repr(data_record.serialize())
        self.device.write(data_record.serialize())
