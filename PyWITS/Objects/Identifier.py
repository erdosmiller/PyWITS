class Identifier:
    def __init__(self,record_identifier=None,item_identifier=None,raw=None):
        """Initializes a Physical Record
        """
        self.record_identifier = record_identifier
        self.item_identifier = item_identifier

        if raw is not None:
            self.construct(raw)

    def serialize(self):
        """Returns a serial representation of the object"""
        return str(self.record_identifier) + str(self.item_identifier)
        
    def construct(self,raw):
        print "??",raw

    def __eq__(self,other):
        if not isinstance(other,Identifier):
            return NotImplemented

        return self.record_identifier == other.record_identifier & self.item_identifier == other.item_identifier

if __name__ == '__main__':
    import unittest
    class IdentifierTests(unittest.TestCase):
        def setUp(self):
            self.test_identifier = Identifier()
            pass
        def tearDown(self):
            pass
        
        def testEQ(self):
            self.failIfEqual(self.test_identifier,None)
            self.failUnlessEqual(self.test_identifier,self.test_identifier)

    unittest.main()
