'''
2. Write a Python program to find out what version of Python you are using.
'''

import unittest
from src import example002

class TestExample002(unittest.TestCase):

    def test_example002(self):
        self.assertEqual(
            example002(),
            '3.12',
		)

if __name__ == '__main__':
    unittest.main()