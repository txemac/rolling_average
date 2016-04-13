import unittest

from rolling_average import get_rolling_averages


__author__ = 'josebermudez'


class TestTask2(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTask2, self).__init__(*args, **kwargs)

    def test_array_none(self):
        self.assertRaises(ValueError, get_rolling_averages, array=None, n=2)

    def test_n_negative(self):
        self.assertRaises(ValueError, get_rolling_averages, array=[1, 2, 3], n=-1)

    def test_array_small(self):
        self.assertRaises(ValueError, get_rolling_averages, array=[1, 2], n=3)

    def test_example(self):
        array = [10, 10, 13, 16, 13, 13]
        n = 3
        expected_response = [11, 13, 14, 14]
        self.assertListEqual(get_rolling_averages(array=array, n=n), expected_response)

    def test_example2(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        n = 3
        expected_response = [2, 3, 4, 5, 6, 7]
        self.assertListEqual(get_rolling_averages(array=array, n=n), expected_response)
