class Domino:
  """
  Represents a singular domino, which has a set of pips on each side.
  Each side can be anywhere from 0-12 pips.
  """
  def __init__(self, side1: int, side2: int) -> None:
    """
    Creates a domino object
    """

    if not 0 <= side1 <= 12:
      raise ValueError
    if not 0 <= side2 <= 12:
      raise ValueError

    self.side1 = side1
    self.side2 = side2
  
  def is_double(self) -> bool:
    return self.side1 == self.side2
  
  def get_score(self) -> int:
    return self.side1 + self.side2
  
  def _flip(self) -> "Domino":
    """
    Returns a new domino that is the original
    domino with sides 1 and 2 switched.
    """
    return Domino(self.side2, self.side1)
  
  def can_connect(self, other: "Domino") -> bool:
    return self.side2 == other.side1
  
  def __str__(self) -> str:
    return f"[{self.side1}, {self.side2}]"

  def __eq__(self, other: "Domino") -> bool:
    return self.side1 == other.side1 and self.side2 == other.side2 or self.side1 == other.side2 and self.side2 == other.side1
  
  def __hash__(self):
    return hash(self.side1, self.side2)