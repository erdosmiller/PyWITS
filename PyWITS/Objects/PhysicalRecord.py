class PhysicalRecord:
    def __init__(self,logical_records):
        """Initializes a Physical Record
        logical_records - A collection of logical_records"""
        self.logical_records = logical_records

    def __eq__(self,other):
        if not isinstance(other,PhysicalRecord):
            return NotImplemented

        return self.logical_records == other.logical_records
        
if __name__ == '__main__':
    import unittest
    class PhysicalRecordTests(unittest.TestCase):
        def setUp(self):
            self.test_physical_record = PhysicalRecord(10)
            pass
        def tearDown(self):
            pass
        
        def testEQ(self):
            self.failIfEqual(self.test_physical_record,None)
            self.failUnlessEqual(self.test_physical_record,self.test_physical_record)

    unittest.main()
