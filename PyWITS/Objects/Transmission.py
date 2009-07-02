from PyWITS.Objects.WITS0.PhysicalRecord import PhysicalRecord

class Transmission:
    def __init__(self):
        self.physical_record = PhysicalRecord()

    
if __name__ == '__main__':
    import unittest
    
    class TransmissionTests(unittest.TestCase):
        def setUp(self):
            self.test_transmission = Transmission()

        def testSetup(self):
            pass

    unittest.main()
    

