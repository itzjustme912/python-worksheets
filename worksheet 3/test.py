import unittest
from worksheet2 import *

# DO NOT CHANGE ANYTHING IN THIS FILE

class TestFunctions(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)

    def test_is_prime(self):
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(28), False)
        self.assertEqual(is_prime(17), True)
        
if __name__ == '__main__':
    unittest.main()
