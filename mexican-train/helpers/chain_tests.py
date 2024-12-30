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


if __name__ == "__main__":
  unittest.main()