from domino import Domino
from typing import Optional

class Chain:
  """
  Essentially a LinkedList that uses a Domino as Node data.
  """
  def __init__(self, spinner: int) -> None:

    if not 0 <= spinner <= 12:
      raise ValueError

    self.__size: int = 0
    self.spinner = spinner
    self.__head: Optional[_Node] = None
    self.__tail: Optional[_Node] = None
  
  def append(self, dom: "Domino") -> bool:
    """
    Appends a domino to the end of the chain. The chain can only successfully be added to if
    the side2 of the tail is the same as the new domino's side1, if side2 matches instead
    the domino will be flipped.

    In the case it is the first domino, a valid append must match the spinner or round of play. 

    Returns T/F based on if the append is successful.
    """
    to_append: _Node = _Node(dom)

    if self.__size == 0:
      if to_append.data.side1 == self.spinner:
        self.__head = to_append
        self.__tail = to_append
        self.__size += 1
        return True
      elif to_append.data.side2 == self.spinner:
        to_append.data._flip()
        self.__head = to_append
        self.__tail = to_append
        self.__size += 1
        return True
      else:
        return False
    
    if to_append.data.side1 == self.__tail.data.side2:
      self.__tail.next = to_append
      self.__tail = to_append
      self.__size += 1
      return True
    elif to_append.data.side2 == self.__tail.data.side2:
      to_append.data._flip()
      self.__tail.next = to_append
      self.__tail = to_append
      self.__size += 1
      return True
    else:
      return False

  def get_total(self) -> int:
    """
    Returns the total score of the chain, being the total sum of domino scores
    it contains.
    """
    total: int = 0
    
    current: _Node = self.__head
    while current is not None:
      total += current.data.get_score()
      current = current.next
    
    return total

class _Node:
  """
  Helper class that holds a domino as data, will be singly linked to the next one.
  """

  def __init__(self, domino: "Domino"):
    self.data: Domino = domino
    self.next: Optional[_Node] = None