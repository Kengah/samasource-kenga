import unittest

from divide import division, summ, floats


class testDivision(unittest.TestCase):
	def test_negative_number(self):
	  self.assertEqual(division(9,-2), -4.5)

class testSumm(unittest.TestCase):
  def test_sum(self):
  	self.assertEqual(summ(4,4), 8)
  	
class test_add_floats(unittest.TestCase):
  def test_float(self):
  	self.assertEqual(floats(3.5,1), 4.5)
  	
    
if __name__ == '__main__':
    unittest.main()