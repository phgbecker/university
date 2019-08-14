import unittest

from fibonacci.Fibonacci import Fibonacci


class FibonacciTest(unittest.TestCase):

    def given_number_when_apply_then_is_equals(self):
        self.assertEqual(Fibonacci.apply(0), 0)
        self.assertEqual(Fibonacci.apply(1), 1)
        self.assertEqual(Fibonacci.apply(2), 1)
        self.assertEqual(Fibonacci.apply(3), 2)
        self.assertEqual(Fibonacci.apply(4), 3)
        self.assertEqual(Fibonacci.apply(5), 5)
        self.assertEqual(Fibonacci.apply(6), 8)
        self.assertEqual(Fibonacci.apply(7), 13)
        self.assertEqual(Fibonacci.apply(8), 21)


if __name__ == '__main__':
    unittest.main()
