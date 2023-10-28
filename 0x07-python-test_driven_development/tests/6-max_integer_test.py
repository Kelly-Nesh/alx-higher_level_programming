#!/usr/bin/python3
"""write unittests for the function def max_int(list=[]):
"""

import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_int."""

    def test_empty_list(self):
        """Testing an empty list."""
        empty_list = []
        self.assertEqual(max_int(empty_list), None)

    def test_singleton_list(self):
        """Test for a singleton list."""
        singleton = [5]
        self.assertEqual(max_int(singleton), 5)

    def test_ordered_list(self):
        """Testing an ordered list of integers."""
        ints = [5, 6, 7, 8, 9]
        self.assertEqual(max_int(ints), 9)

    def test_max_first(self):
        """Test for a list with max value first."""
        max_first = [9, 8, 7, 6, 5]
        self.assertEqual(max_int(max_first), 9)

    def test_unordered_ints(self):
        """Test an unordered list of integers."""
        ints = [5, 8, 7, 9, 6]
        self.assertEqual(max_int(ints), 9)

    def test_floats(self):
        """Testing a list of floats."""
        fl = [0.53, 16.45, -29.123, 25.4, 23.0]
        self.assertEqual(max_int(fl), 25.4)

    def test_ints_and_floats(self):
        """Testing a list of ints and floats."""
        inf = [0.21, 25.4, -29, 25, 16]
        self.assertEqual(max_int(inf), 25.4)

    def test_empty_string(self):
        """Testing an empty string."""
        self.assertEqual(max_int(""), None)

    def test_string(self):
        """Testing a string."""
        test_string = "johnathan"
        self.assertEqual(max_int(test_string), 't')

    def test_list_strings(self):
        """Test a list strings."""
        test_strings = ["jonahthan", "barklay", "mygoly", "name"]
        self.assertEqual(max_int(test_strings), "name")

if __name__ == '__main__':
    unittest.main()
