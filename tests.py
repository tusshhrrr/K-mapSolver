# Roll No.:2018201
# Name:Tushar
# Section:A
# Group:1
#CSE-IP HW-2
#K-Map minimization


import unittest
from HW2_2018201 import *



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(2,"(0,1) d(2,3)"),"1")
		self.assertEqual(minFunc(2,"() d(0,1,2,3)"),"0")
		self.assertEqual(minFunc(2, "(0,3) d(2)"), "w+x'")
		self.assertEqual(minFunc(2, "(0,1) d()"), "w'")
		self.assertEqual(minFunc(2, "(0,3) d()"), "w'x'+wx")
		self.assertEqual(minFunc(3, "(0,1,5,6,7) d()"), "w'x'+wx+wy")
		self.assertEqual(minFunc(3, "(6,7) d(0,1,2,3)"), "x")
		self.assertEqual(minFunc(3, "(3,5,7) d(0)"), "wy+xy")
		self.assertEqual(minFunc(3, "() d()"), "0")
		self.assertEqual(minFunc(3, "(1,4,7) d(2,3)"), "w'y+wx'y'+xy")
		self.assertEqual(minFunc(4, "(8,9,10,11) d(12,13,14,15)"), "w")
		self.assertEqual(minFunc(4, "(1,2,4,7,8) d(9,10,12)"), "w'xyz+wy'z'+x'y'z+x'yz'+xy'z'")
		self.assertEqual(minFunc(4, "(1,2,4) d(9,10,12)"), "x'y'z+x'yz'+xy'z'")
		self.assertEqual(minFunc(4, "(1) d(0,10,11,12,13,14,15)"), "w'x'y'")
		self.assertEqual(minFunc(4, "(0,1,2,3,4,7,8) d(9,10,11,12,13,14,15)"), "x'+y'z'+yz")








		
                
if __name__=='__main__':
	unittest.main()
