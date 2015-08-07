import unittest
import ordinal

class Testordinal(unittest.TestCase):
	def setUp(self):
		self.value = 1
		
	def test_first(self):
		self.assertEqual(ordinal.ordinal(self.value), "1st")
	def test_second(self):
		self.assertEqual(ordinal.ordinal(2), "2nd")
	def test_third(self):
		self.assertEqual(ordinal.ordinal(3), "3rd")
	def test_eleven(self):
		self.assertNotEqual(ordinal.ordinal(111), "111st")
	def test_other(self):
		self.assertEqual(ordinal.ordinal(34), "34th")		
		
if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()