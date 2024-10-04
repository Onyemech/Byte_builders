from unttest import TestCase
from exchange import exchange


	def test_that_convert_currency_function_exist(self):
		convert_currency(100)

	def test_that_convert_currency_function_return_correc_value(self):
		self.assertEqual(convert_currency(10) , 15500)
		self.assertEqual(convert_currency(20.1) , 31_155)

	def test_that_convert_currency_function_return_correc_value(self):
		self.assertEqual(convert_currency(20.1) , 31_155)
		self.assertEqual(convert_currency(35.25) , 54637.5)

	def test_that_convert_currency_function_raise_error_with_negative_value(self):
		self.assertRaises(ValueError, convert_currency, -12)
	
	def test_that_convert_currency_function_raise_error_with_String_value(self):
		self.assertEqual(convert_currency("Williams - Gstring") , "Invalid input")
		self.assertEqual(convert_currency("") , "Invalid input")

class TestDivideOrSquare(TestCase):
	
	def test_that_divide_or_square_function_exist(self):
		divide_or_square(1)
	
	def test_that_convert_currency_function_raise_error_with_String_value(self):
		self.assertEqual(divide_or_square(10) , 3)
