# -*- coding: utf-8 -*-
# Unittest av gange-funksjon.
# Gruppenr.: 13
# Medlemmer: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
import unittest
from aritmetic import gange


class TestGange(unittest.TestCase):
    def setUp(self):
        pass
    def test_positive_positive(self):
        self.assertEqual(gange(10,10), 100)
        
    def test_negative_positive(self):
        self.assertEqual(gange(-40,45), -1800)
        
    def test_decimal(self):
        self.assertEqual(gange(10.5,77.2), 810.6)
        
    def test_large_numbers(self):
        self.assertEqual(gange(976426,2023574), 1975870266524)
        
    def test_large_positive_negative(self):
        self.assertEqual(gange(47056,-27000), -1270512000)
    
    def test_large_decimal(self):
        self.assertEqual(gange(1000000.05, 999999.55), 999999599999.9775)
        
if __name__ == '__main__':
    unittest.main()