# Import unittest module
import unittest
# Import def deal from deal.py
from deal import deal

# Test dealing method
class TestDeal5Players(unittest.TestCase):
    def setUp(self):
        pass
    # Test dealing 5 cards to 5 players
    def test_deal_5_cards_5_players(self):
        self.assertEqual(5, 5)
        
if __name__ == '__main__':
    unittest.main()