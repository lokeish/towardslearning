import unittest


def sum_two_numbers(a, b):
    return a + b


class TestSample(unittest.TestCase):
    def test_sum_two_numbers(self):
        result = sum_two_numbers(1, 2)
        self.assertEqual(3, result)

    def test_sum_two_numbers_wrong_input(self):
        result = sum_two_numbers(2, 5)
        self.assertEqual(10, result)
