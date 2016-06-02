# -*- coding: utf-8 -*-
# Unittest av minus-funksjon.
# Gruppenr.: 13
# Medlemmer: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
import unittest
from aritmetic import minus


class TestMinus(unittest.TestCase):
    def setUp(self):
        pass
    def test_positive_positive(self):
        self.assertEqual(minus(55,15), 40)
        
    def test_negative_positive(self):
        self.assertEqual(minus(-45,5), -50)
        
    def test_decimal(self):
        self.assertEqual(minus(251.2,52.1), 199.1)
        
    def test_large_numbers(self):
        self.assertEqual(minus(20072366,7598832), 12473534)
        
    def test_large_positive_negative(self):
        self.assertEqual(minus(153000000,-76900000), 229900000)
    
    def test_large_decimal(self):
        self.assertEqual(minus(1000000.05, 999999.55), 0.5)
        
if __name__ == '__main__':
    unittest.main()