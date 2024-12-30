from domino import *
import unittest

class DominoTest(unittest.TestCase):

  def setUp(self) -> None:
    self.dom = Domino(1, 12)
  
  def test_flip0(self) -> None:
    self.dom._flip()

    self.assertEqual(self.dom.side1, 12)
    self.assertEqual(self.dom.side2, 1)
  

if __name__ == "__main__":
  unittest.main()