# Test cases for Project Euler helper functions
# syntaxaire

import unittest
import itertools
from euler import *


class TestEulerHelpers(unittest.TestCase):

    def test_prime_factors(self):
        # self.assertRaises(ValueError, prime_factors, -100)
        # self.assertRaises(ValueError, prime_factors, -1)
        # self.assertRaises(ValueError, prime_factors, 0)
        # self.assertRaises(ValueError, prime_factors, 1)
        self.assertEquals(prime_factors(2), [2])
        self.assertEqual(prime_factors(3), [3])
        self.assertEqual(prime_factors(35), [5, 7])
        self.assertEqual(prime_factors(2**32), [2]*32)

    def test_lcm(self):
        self.assertEquals(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2520)

    def test_prime_sieve(self):
        def do_tests(sievefunc):
            self.assertEqual(sievefunc(2), [2])
            self.assertEqual(sievefunc(21), [2, 3, 5, 7, 11, 13, 17, 19])
            self.assertEqual(sum(sievefunc(100000)), 454396537)

        do_tests(sieve_eratosthenes_up_to)

    def test_digit_product(self):
        self.assertEqual(digit_product('0'), 0)
        self.assertEqual(digit_product('1'), 1)
        self.assertEqual(digit_product('2'), 2)
        self.assertEqual(digit_product('10'), 0)
        self.assertEqual(digit_product('21'), 2)
        self.assertEqual(digit_product('2225'), 40)

    def test_factor_list(self):
        self.assertEqual(factor_list(1), [1])
        self.assertEqual(factor_list(2), [1, 2])
        self.assertEqual(factor_list(20), [1, 2, 4, 5, 10, 20])

    def test_gen_triangular_numbers(self):
        trigen = gen_triangular_numbers()
        test = list(itertools.islice(trigen, 10))
        self.assertEqual(test, [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

    def test_gen_fibonacci(self):
        fibgen = gen_fibonacci()
        test = list(itertools.islice(fibgen, 10))
        self.assertEqual(test, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

if __name__ == '__main__':
    unittest.main(verbosity=2)
