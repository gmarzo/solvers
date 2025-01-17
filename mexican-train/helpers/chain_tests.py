from domino import *
from chain import *
import unittest

class ChainTest(unittest.TestCase):

  def setUp(self):
    self.train6: "Chain" = Chain(6)
  
  def test_append0(self):
    self.assertTrue(self.train6.append(Domino(6, 3)))
    self.assertTrue(self.train6.append(Domino(3, 2)))
    self.assertTrue(self.train6.append(Domino(2, 7)))
    self.assertTrue(self.train6.append(Domino(7, 4)))
  
  def test_append1(self):
    self.assertFalse(self.train6.append(Domino(1, 1)))

    self.assertTrue(self.train6.append(Domino(6, 9)))
    self.assertTrue(self.train6.append(Domino(0, 9)))
    self.assertTrue(self.train6.append(Domino(0, 3)))
  
  def test_str0(self):
    self.assertTrue(self.train6.append(Domino(6, 4)))
    self.assertTrue(self.train6.append(Domino(4, 3)))
    self.assertTrue(self.train6.append(Domino(3, 7)))

    self.assertTrue(str(self.train6), "[6, 4][4, 3][3, 7]")
  
  def test_flip0(self):
    self.assertTrue(self.train6.append(Domino(6, 4)))
    self.assertTrue(self.train6.append(Domino(4, 3)))
    self.assertTrue(self.train6.append(Domino(3, 7)))

    self.assertTrue(str(self.train6), "[6, 4][4, 3][3, 7]")

    self.train6.flip()

    self.assertTrue(str(self.train6), "[7, 3][3, 4][4, 6]")


if __name__ == "__main__":
  unittest.main()