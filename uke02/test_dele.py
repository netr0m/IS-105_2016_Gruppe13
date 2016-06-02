# -*- coding: utf-8 -*-
# Unittest av dele-funksjon.
# Gruppenr.: 13
# Medlemmer: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
import unittest
from aritmetic import dele


class TestDele(unittest.TestCase):
    def setUp(self):
        pass
    def test_positive_positive(self):
        self.assertEqual(dele(100,10), 10)
        
    def test_negative_positive(self):      # Her ville unittest runde opp til 1. Det egentlige (kalkulator) resultatet under:
        self.assertEqual(dele(-40,45), -1) # -0.8888888888888889
        
    def test_decimal(self):                                   # Her ble unittestens svar det samme som det egentlige (kalkulator) resultatet.
        self.assertEqual(dele(10.5,77.2), 0.1360103626943005) # 0.1360103626943005
        
    def test_large_numbers(self):               # # Her ville unittest runde ned til 8. Det egentlige (kalkulator) resultatet under:
        self.assertEqual(dele(500000,55600), 8) # 8.992805755395683
        
    def test_large_positive_negative(self):      # # Her ville unittest runde opp til 2. Det egentlige (kalkulator) resultatet under:
        self.assertEqual(dele(47056,-27000), -2) # -1.742814814814815
    
    def test_large_decimal(self):                                        # Her ble unittestens svar det samme som det egentlige (kalkulator) resultatet. 
        self.assertEqual(dele(1000000.05, 999999.55), 1.000000500000225) # 1.000000500000225
        
if __name__ == '__main__':
    unittest.main()