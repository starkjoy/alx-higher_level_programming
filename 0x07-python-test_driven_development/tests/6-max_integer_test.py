#!/usr/bin/python3
""" This runs a unittest on a function """


import unittest
import importlib
module_name = "6-max_integer"
module = importlib.import_module(module_name)
max_integer = module.max_integer

class TestMaxInteger(unittest.TestCase):
    """ Tests max_integer function """

    def test_empty_list(self):
        """ Tests for empty list """
        self.assertIsNone(max_integer([]))
    def test_positive_numbers(self):
        """ Tests for list of positive numbers """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    def test_negative_numbers(self):
        """ Tests for list of negative numbers """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    def test_mixed_numbers(self):
        """ Tests for list of mixed numbers """
        self.assertEqual(max_integer([1, 2, -3, -4, 5]), 5)
    def test_duplicate_numbers(self):
        """ Tests for list of duplicate numbers """
        self.assertEqual(max_integer([1, 2, 2, 4, 5]), 5)
    def test_single_item_list(self):
        """ Test for a list conataining a single item """
        self.assertEqual(max_integer([5]), 5)

if __name__ == '__main__':
    unittest.main()
