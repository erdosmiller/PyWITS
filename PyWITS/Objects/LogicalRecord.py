class LogicalRecord:
    def __init__(self,data_record):
        """Initializes a LogicalRecord
        data_record - the data_record of the logical record
        """
        self.data_record = data_record


    def __eq__(self,other):
        if not isinstance(other,LogicalRecord):
            return NotImplemented
        x
        return self.data_record == other.data_record

if __name__ == '__main__':
    import unittest
    class LogicalRecordTests(unittest.TestCase):
        def setUp(self):
            self.test_logical_record = LogicalRecord(10)
            pass

        def tearDown(self):
            pass
        
        def testEQ(self):
            self.failIfEqual(self.test_logical_record,None)
            self.failUnlessEqual(self.test_logical_record,self.test_logical_record)
        
    unittest.main()
