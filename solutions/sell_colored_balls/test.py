import unittest

from .solution import maxProfit

class TestCase(unittest.TestCase):

    def test_example_one(self):
        inventory = [2,5]
        orders = 4
        self.assertEqual(maxProfit(inventory, orders), 14)

    def test_example_two(self):
        inventory = [3,5]
        orders = 6
        self.assertEqual(maxProfit(inventory, orders), 19)

    def test_example_three(self):
        inventory = [2,8,4,10,6]
        orders = 20
        self.assertEqual(maxProfit(inventory, orders), 110)

    def test_example_four(self):
        inventory = [1000000000]
        orders = 1000000000
        self.assertEqual(maxProfit(inventory, orders), 21)