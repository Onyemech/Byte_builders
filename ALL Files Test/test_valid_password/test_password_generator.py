import unittest
import password_generator

class TestPasswordGenerator(unittest.TestCase):
	def test_that_function_exist(self):
		password_generator.generate_password(password)
	def test_that_function_returns_uppercase_and_lowercase(self):
		self.assertEqual(password_generator.generate_password())