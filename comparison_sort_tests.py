""" Lab 6 Test Suite
Chris Specht
Koichi Kodama
CPE 202-09
Spring 2019
Due Friday, May 17th
"""


import unittest
from comparison_sort import *


class TestCase(unittest.TestCase):

    def test_bubble_sort(self):
        ints = [5, 4, 3, 2, 1]
        bubble_sort(ints)
        self.assertEqual(ints, [1, 2, 3, 4, 5])

    def test_bubble_sort2(self):
        ints = [5, 4, 3, 2, 1]
        bubble_sort2(ints)
        self.assertEqual(ints, [1, 2, 3, 4, 5])

    def test_merge_sort(self):
        ints = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(ints), ([1, 2, 3, 4, 5], 7))

    def test_merge(self):
        ints1 = [1, 3, 5]
        ints2 = [2, 4, 6]
        self.assertEqual(merge(ints1, ints2, None), ([1, 2, 3, 4, 5, 6], 5))


def main():
    unittest.main()


if __name__ == "__main__":
    main()