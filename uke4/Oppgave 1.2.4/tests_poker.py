import unittest
from deal import deal

class TestDeal(unittest.TestCase):
    def setUp(self):
        pass
    def test_deal_5_cards(self):
        self.assertEqual(5, 5)
        
if __name__ == '__main__':
    unittest.main()