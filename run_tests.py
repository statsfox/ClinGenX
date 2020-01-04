"""
run_tests.py

unit tests for ClinGenX.py

"""

import unittest
from Bedline import Bedline
from Chr import Chr

class MyTestCase(unittest.TestCase):

    def test_chr_format_chr(self):
        chr = Chr("chr23")
        self.assertEqual(chr.seq, 'X')
    def test_chr_format_CHR(self):
        chr = Chr("CHR24")
        self.assertEqual(chr.seq, 'Y')
    def test_chr_format_Chr(self):
        chr = Chr("Chr25")
        self.assertEqual(chr.seq, 'MT')

class ExpectedFails(unittest.TestCase):
    @unittest.expectedFailure
    def test_chr_incorrect(self):
        chr = Chr("26")
    @unittest.expectedFailure
    def test_chr_with_spaces(self):
        chr = Chr("1 2")

if __name__ == '__main__':
    unittest.main()
