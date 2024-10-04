import unittest
import squareroot

class TestExchangeRate(unittest.TestCase):

	def  test_squareroot_function_exist(self) :
		squareroot.get_squareroot(10)

	def test_squareroot_function__raise_error_with_negative_amount(self) :
		self.assertRaises(ValueError,squareroot.get_squareroot, -100)
