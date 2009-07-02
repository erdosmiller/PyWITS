from PyWITS import Globals

class DataItem:
    def __init__(self,identifier=None,value=None,raw=None):
        """Initializes a Physical Record
        """
        self.identifier = identifier
        self.value = value

        if raw is not None:
            self.construct(raw)

    def serialize(self):
        """Returns a serial representation of the object"""
        #serialize the identifier
        ser_str = self.identifier.serialize()

        #serial the value
        ser_str += str(self.value)
        
        #add the seperator
        ser_str += Globals.DATA_ITEM_SEPERATOR
        #return the string
        return ser_str
            
    def construct(self,raw):
        import string
        from PyWITS.Objects.Identifier import Identifier

        raw = string.strip(raw)
        
        self.identifier = Identifier(raw=raw[0:3])

        self.value = float(raw[4:])
        
        
    
    def __eq__(self,other):
        if not isinstance(other,DataItem):
            return NotImplemented

        return self.identifier == other.identifier & self.value ==  other.value

if __name__ == '__main__':
    import unittest
    class DataItemTests(unittest.TestCase):
        def setUp(self):
            self.test_data_item = DataItem()
            pass
        def tearDown(self):
            pass
        
        def testEQ(self):
            self.failIfEqual(self.test_data_item,None)
            self.failUnlessEqual(self.test_data_item,self.test_data_item)

    unittest.main()
