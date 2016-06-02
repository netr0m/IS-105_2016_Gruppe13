# -*- coding: utf-8 -*-
# Unittest av pluss-funksjon.
# Gruppenr.: 13
# Medlemmer: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
import unittest
from aritmetic import pluss


class TestPluss(unittest.TestCase):
    def setUp(self):
        pass
    def test_positive_positive(self):
        self.assertEqual(pluss(10,10), 20)
        
    def test_negative_positive(self):
        self.assertEqual(pluss(-40,45), 5)
        
    def test_decimal(self):
        self.assertEqual(pluss(10.5,77.2), 87.7)
        
    def test_large_numbers(self):
        self.assertEqual(pluss(976426,2023574), 3000000)
        
    def test_large_positive_negative(self):
        self.assertEqual(pluss(153000000,-76900000), 76100000)
    
    def test_large_decimal(self):
        self.assertEqual(pluss(1000000.05, 999999.55), 1999999.6)
        
if __name__ == '__main__':
    unittest.main()