# -*- coding: utf-8 -*-
# Unittest av kvadratrot-funksjon.
# Gruppenr.: 13
# Medlemmer: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
import unittest
from aritmetic import kvadratrot


class TestKvadratrot(unittest.TestCase):
    def setUp(self):
        pass
    def test_positive_positive(self):
        self.assertEqual(kvadratrot(3,3), 9)
        
    def test_decimal(self):
        self.assertEqual(kvadratrot(1.82,1.82), 3.3124000000000002)
        
    def test_large_numbers(self):
        self.assertEqual(kvadratrot(1024,1024), 1048576)
    
    def test_large_decimal(self):
        self.assertEqual(kvadratrot(81.15, 81.15), 6585.322500000001)
        
if __name__ == '__main__':
    unittest.main()