"""
run_tests.py

unit tests for ClinGenX.py

"""

import unittest
from Bedline import Bedline


class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_chr_format(self):
        bedline = Bedline(1, 1000, 200)

if __name__ == '__main__':
    unittest.main()
