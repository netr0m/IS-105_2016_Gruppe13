# Import unittest module
import unittest
# Import def deal from deal.py
from encode_decode import code, encode, decode

# Test encoding
class TestEncode(unittest.TestCase):
    def setUp(self):
        pass
    # Test encoding the given string
    def test_encode_string(self):
        self.assertEqual("Norway stun Poland 30:28 and spoil Bielecki's birthday party.")

# Test decoding
class TestDecode(unittest.TestCase):
    def setUp(self):
        pass
    # Test decoding the given file
    def test_decode_file(self):
        self.assertEqual('sourcecode.txt', 8, code())
        
if __name__ == '__main__':
    unittest.main()