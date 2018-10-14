import unittest

from calculator import calculate
from calculator import str_calculate

class TestCalcurator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)

    def test_odejmowanie(self):
        r = calculate(5, 2, '-')
        self.assertEqual(r, 3)

    def test_mnozenie(self):
        r = calculate(2, 3, '*')
        self.assertEqual(r, 6)

    def test_dzielenie(self):
        r = calculate(6, 2, '/')
        self.assertEqual(r, 3)

class TestStringCalcurator(unittest.TestCase):
    def test_concat(self):
        r = str_calculate("a", "b", 'concat')
        self.assertEqual(r, 'ab')
