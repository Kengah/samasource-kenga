import unittest

from division import division


class testdivision_positive_number(unittest.TestCase):
	def testdivision_positive_number(self):
	  self.assertEqual(division(4,4), 1)
	  self.assertEqual(division(12,2), 6)
	  
class testdivision_negative_number(unittest.TestCase):
	def testdivision_negative_number(self):
	  self.assertEqual(division(-9,-2), 4.5)
	  self.assertEqual(division(-6,-3), 2)
	  
	def test_division_by_zero_exception(self):
	  self.assertRaises(ZeroDivisionError)
	
  	
class testdivision_floats(unittest.TestCase):
  def testdivision_floats(self):
  	self.assertEqual(division(4.5,1.5),3.0)
  	self.assertEqual(division(6.25,2.5), 2.5)

    
if __name__ == '__main__':
    unittest.main()