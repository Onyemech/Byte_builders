import unittest
import swap_numbers

class TestSwap_numbers(unittest.TestCase):
	def test_that_list_function_exist(self):
		swap_numbers.lists([1, 2, 3, 4, 5, 6])
	def test_that_list_function_returns_swapped_values(self):
		elements = [1, 2, 3, 4, 5, 6]
		result = [2, 1, 4, 3, 6, 5]
		self.assertEqual(swap_numbers.lists(elements), result)