'''
2. Write a Python program to find out what version of Python you are using.
'''

import unittest
from src.example999 import *


class TestExample999(unittest.TestCase):

    def test_example999(self):
        self.assertEqual(
            example999(''),
            '',
        )

    def test_covariance(self):
        a = A()
        b = B()

        print_co(I_co(a))
        print_co(I_co(b))

    def test_contravariant(self):
        a = A()
        b = B()

        print_contra(I_contra(a))
        print_contra(I_contra(b))


if __name__ == '__main__':
    unittest.main()
