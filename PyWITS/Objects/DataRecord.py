from PyWITS import Globals

class DataRecord:
    def __init__(self,data_items=None,raw=None):
        """Initializes a DataRecord
        """

        if data_items is None:
            self.data_items = []
        else:
            self.data_items = data_items

        if raw is not None:
            self.construct(raw)

    def serialize(self):
        #start the record
        ser_str = Globals.DATA_RECORD_BEGIN
        
        #for each data item
        for data_item in self.data_items:
            #append it to the record
            ser_str += data_item.serialize()

        #end the record
        ser_str += Globals.DATA_RECORD_END
        
        return ser_str

    def construct(self,raw):
        import re

        from PyWITS.Objects.DataItem import DataItem

        #compile the re to match the data_set format
        data_item_re = re.compile('[^!^&^\r^\n]+\r\n')
        #find the raw data items
        raw_data_items = data_item_re.findall(raw)

        data_items = []
        for raw_data_item in raw_data_items:
            data_items.append(DataItem(raw=raw_data_item))
        

    def __eq__(self,other):
        if not isinstance(other,DataRecord):
            return NotImplemented

        return self.data_items == other.data_items

if __name__ == '__main__':
    import unittest
    class DataRecordTests(unittest.TestCase):
        def setUp(self):
            self.test_data_record = DataRecord(10)
            pass

        def tearDown(self):
            pass
        
        def testEQ(self):
            self.failIfEqual(self.test_data_record,None)
            self.failUnlessEqual(self.test_data_record,self.test_data_record)
        
    unittest.main()
