import unittest
from CI-test.calcul.addition import *

class TestCalcul(unittest.TestCase) :
 
	def test_calcul(self) :
		resultat = addition(5, 2)
		self.assertEqual(resultat, 7)
        

if __name__ == '__main__':
	unittest.main()