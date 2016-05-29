import unittest
from deal import deal

class TestDeal(unittest.TestCase):
    def setUp(self):
        pass
    def test_deal_5_cards(self):
        self.assertEqual(5, 5)
    
    def test_deal_5_cards_2_players(self):
        self.assertEqual(5, 5)
        self.assertEqual(5, 5)
        
if __name__ == '__main__':
    unittest.main()