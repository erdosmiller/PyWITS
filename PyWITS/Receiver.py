from PyWITS import Globals
from PyWITS.Objects.DataRecord import DataRecord

def WITS0(func):
    def inner_func(*args,**kwargs):
        import re

        obj = args[0] #get the class

        if obj.mode == 0: #make sure we're in WITS0 mode
            pass

        data = func(*args,**kwargs) #call the function
        
        

        if obj.mode == 0: #make sure we're in WITS0 mode again

            #regular expression, match the start and end, but not the start and end characters
            set_re = re.compile(Globals.DATA_RECORD_BEGIN + '[^&^!]*' + Globals.DATA_RECORD_END,re.DOTALL) 

            #after we call the re the data should be split up into raw data records
            data_records = set_re.findall(data)
            
            new_data_records = [] #to hold the new data records

            for data_record in data_records: #for each raw data set
                new_data_records.append(DataRecord(raw=data_record))
                
            return data_records
        
        #if we're not in WITS0 mode, return the plain data
        return data

    return inner_func

class Receiver:
    def __init__(self,device,mode=0):
        self.device = device
        self.mode = mode

    def ask(self,question):
        self.device.write(question)
        return self.read()
 
    #@WITS0
    def read(self):
        data = ''
        new_data = None
        while(new_data != ''):
            new_data = self.device.read()
            data += new_data
        print repr(data)

        return data

    
        

if __name__ == '__main__':
    import unittest
    import serial

    class ReceiverTestCases(unittest.TestCase):
        def setUp(self):
            pass
        def tearDown(self):
            pass

    unittest.main()

