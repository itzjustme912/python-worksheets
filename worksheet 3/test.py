import unittest
from worksheet2 import *

# DO NOT CHANGE ANYTHING IN THIS FILE

class TestFunctions(unittest.TestCase):

    def test_n_sum(self):
        self.assertEqual(n_sum(10), 55)
        self.assertEqual(n_sum(100), 5050)

    def test_n_cubes(self):
        self.assertEqual(n_cubes(5), [1,8,27,64,125])
        self.assertEqual(n_cubes(7), [1,8,27,64,125, 216, 343])

    def test_string_concatenation(self):
        self.assertEqual(string_concatenation('poke', 'mon'), 'pokemon')
        self.assertEqual(string_concatenation('mone', 'amore'), 'moneamore')
        self.assertEqual(string_concatenation('palin', 'drome'), 'palindrome')

    def test_is_even(self):
        self.assertEqual(is_even(39723057024857), False)
        self.assertEqual(is_even(397230570244), True)

    def test_first_n_divisible_numbers(self):
        self.assertEqual(first_n_divisible_numbers(7,7), [7,14,21,28,35,42,49])
        self.assertEqual(first_n_divisible_numbers(2,546), [546, 1092])

if __name__ == '__main__':
    unittest.main()
