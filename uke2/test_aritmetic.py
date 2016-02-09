# -*- coding: utf-8 -*-
# Unittest av aritmetiske funksjoner.
# Gruppenr.: 13
# Medlemmer: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
import unittest
from aritmetic import pluss, minus, gange, dele, rest, kvadratrot


class TestPluss(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_10_10(self):
        self.assertEqual(pluss(10,10), 20)

class TestMinus(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_20_5(self):
        self.assertEqual(minus(20,5), 15)
        
class TestGange(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_2_10(self):
        self.assertEqual(gange(2,10), 20) 
        
class TestDele(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_100_10(self):
        self.assertEqual(dele(100,10), 10)
        
class TestResterende(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_20_19(self):
        self.assertEqual(rest(20,19), 1)

class TestKvadratrot(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_2_2(self):
        self.assertEqual(kvadratrot(2,2), 4)

if __name__ == '__main__':
    unittest.main()