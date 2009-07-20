import unittest, string, re, time, socket
from wits0 import *
from packet import *
from mock import *

class TestIOUnimplementedMethods(unittest.TestCase):
    def setUp(self): 
        self.io = IO()

    def testWrite(self):
        self.assertRaises(NotImplementedError, self.io.write, None)
    
    def testRead(self):
        self.assertRaises(NotImplementedError, self.io.read)
        
    def testClose(self):
        self.assertRaises(NotImplementedError, self.io.close)

class MockSerial(object):
    def write(self, data): pass
    def read(self): pass
    def close(self): pass

def CreateMockSerial():
    ms = MockSerial()
    ms.write = Mock()
    ms.read = Mock()
    ms.close = Mock()
    return ms

class MockTCP(object):
    def send(self, data): pass
    def settimeout(self, timeout): pass
    def recv(self, bytes): pass
    def close(self): pass

def CreateMockTCP():
    mtcp = MockTCP()
    mtcp.send = Mock()
    mtcp.settimeout = Mock()
    mtcp.recv = Mock()
    mtcp.close = Mock()
    return mtcp

class TestSerialIO(unittest.TestCase):
    def testWrite(self):
        serial = CreateMockSerial()
        io = SerialIO(serial)

        io.write("foo")
        serial.write.assert_called_with("foo")
        
    def testRead(self):
        serial = CreateMockSerial()
        io = SerialIO(serial)

        serial.read.return_value = ''
        io.read()
        assert serial.read.called
        
    def testClose(self):
        serial = CreateMockSerial()
        io = SerialIO(serial)

        io.close()
        assert serial.close.called

class TestTCPIO(unittest.TestCase):
    def testWrite(self):
        tcp = CreateMockTCP()
        io = TCPIO(tcp)
        
        io.write("blah")
        tcp.send.assert_called_with("blah")

    def testRead(self):
        tcp = CreateMockTCP()
        io = TCPIO(tcp)

        def throwException(*args, **kwargs):
            raise Exception        
        tcp.recv = Mock(side_effect = throwException)

        io.read()
        self.assertTrue(tcp.recv.called, "tcp.recv() was called")
        tcp.settimeout.assert_called_with(0.25)

    def testClose(self):
        tcp = CreateMockTCP()
        io = TCPIO(tcp)
        
        io.close()
        self.assertTrue(tcp.close.called, "tcp.close() was called")

class TestParser(unittest.TestCase):
    def testParse(self):
        p = Parser()
        self.assertRaises(NotImplementedError, p.parse, None)

class TestWITS0Parser(unittest.TestCase):
    def setUp(self):
        self.parser = WITS0Parser()

    def testParse(self):
        test_string = (LogicalRecord.BEGIN + '0111-9999' +
                       DataRecord.SEPERATOR + LogicalRecord.END)
        records = self.parser.parse(test_string)
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(len(record.data_records), 1)
        data_record = record.data_records[0]

        self.assertEqual(data_record.identifier.record, '01')
        self.assertEqual(data_record.identifier.item, '11')
        self.assertEqual(data_record.value, '-9999')

class TestCommunicator(unittest.TestCase):
    def setUp(self):
        io = IO()
        io.write = Mock()
        io.read = Mock()
        io.close = Mock()
        self.io = io

        parser = Parser()
        parser.parse = Mock()
        self.parser = parser
        
    def testWrite(self):
        com = Communicator(self.io, self.parser)
        com.write("foo")
        self.io.write.assert_called_with("foo")
        self.io.write.reset_mock()
        
    def testAsk(self):
        self.io.read.return_value = "baz"
        com = Communicator(self.io, self.parser)

        com.ask("bar")
        self.io.write.assert_called_with("bar")
        self.assertTrue(self.io.read.called)
        self.parser.parse.assert_called_with("baz")

        self.io.write.reset_mock()
        self.parser.parse.reset_mock()

    def testRead(self):
        self.io.read.return_value = "baz"
        com = Communicator(self.io, self.parser)
        com.read()
        self.failUnless(self.io.read.called)
        self.parser.parse.assert_called_with("baz")

        self.parser.parse.reset_mock()
        self.io.read.reset_mock()

    def testClose(self):
        com = Communicator(self.io, self.parser)
        com.close()
        self.failUnless(self.io.close.called)


if __name__ == '__main__':
    unittest.main()

    

    
