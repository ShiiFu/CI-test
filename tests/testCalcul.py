import unittest
from calcul.addition import *

class TestCalcul(unittest.TestCase) :
 
	def test_calcul1(self) :
		resultat = addition(5, 2)
		self.assertEqual(resultat, 7)
 
	def test_calcul2(self) :
		resultat = addition(17, 18)
		self.assertEqual(resultat, 35)
 
	def test_calcul3(self) :
		resultat = addition(2555, 445)
		self.assertEqual(resultat, 3000)

if __name__ == '__main__':
	unittest.main()