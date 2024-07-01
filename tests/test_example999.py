'''
2. Write a Python program to find out what version of Python you are using.
'''

import unittest
from src import example999

class TestExample999(unittest.TestCase):

    def test_example999(self):
        self.assertEqual(
            example999(),
            '3.12',
		)

if __name__ == '__main__':
    unittest.main()