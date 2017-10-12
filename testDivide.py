import unittest

from divide import division, summ, floats, strings


class testDivision(unittest.TestCase):
	def test_negative_number(self):
	  self.assertEqual(division(9,-2), -4.5)
	  self.assertEqual(division(-6,-3), 2)
	  
	def test_division_by_zero_exception(self):
	  self.assertRaises(ZeroDivisionError)
	  

class testSumm(unittest.TestCase):
  def test_sum(self):
  	self.assertEqual(summ(4,4), 8)
  	self.assertEqual(summ(3,-2), 1)
  	
class testStrings(unittest.TestCase):
  def test_strings(self):
  	self.assertEqual(strings('abc','def'),'abcdef')

##@unittest.skip('Skip this test')
  	
class test_add_floats(unittest.TestCase):
  def test_float(self):
  	self.assertEqual(floats(3.5,1), 4.5)
  	self.assertEqual(floats(3.5,1.3), 4.8)

    
if __name__ == '__main__':
    unittest.main()