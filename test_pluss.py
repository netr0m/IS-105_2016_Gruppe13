# -*- coding: utf-8 -*-
# Unittest av pluss funksjon
# Nora Krogh

import unittest
from pluss_script import pluss


class TestPluss(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_10_10(self):
        self.assertEqual(pluss(10,10), 20)
        
if __name__ == '__main__':
    unittest.main()