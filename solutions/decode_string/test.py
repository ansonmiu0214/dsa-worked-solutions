import unittest
from .solution import decodeString

class TestCase(unittest.TestCase):

    def test_example_one(self):
        s = '3[a]2[bc]'
        self.assertEqual(decodeString(s), 'aaabcbc')
    
    def test_example_two(self):
        s = '3[a2[c]]'
        self.assertEqual(decodeString(s), 'accaccacc')

    def test_example_three(self):
        s = '2[abc]3[cd]ef'
        self.assertEqual(decodeString(s), 'abcabccdcdcdef')

    def test_example_four(self):
        s = 'abc3[cd]xyz'
        self.assertEqual(decodeString(s), 'abccdcdcdxyz')