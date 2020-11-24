import unittest
from .solution import calculate

class TestCase(unittest.TestCase):

    def test_literal(self):
        self.assertEqual(calculate('1'), 1)

    def test_literal_with_space(self):
        self.assertEqual(calculate('  1 '), 1)

    def test_plus_minus(self):
        self.assertEqual(calculate('1 + 2 - 3'), 0)

    def test_multiply_divide(self):
        self.assertEqual(calculate('4 * 6 / 3'), 8)

    def test_division_truncate_towards_zero(self):
        self.assertEqual(calculate('5/3'), 1)

    def test_mixed_operations_one(self):
        self.assertEqual(calculate('3+2*2'), 7)

    def test_mixed_operations_two(self):
        self.assertEqual(calculate('3 + 5 / 2'), 5)