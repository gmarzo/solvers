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
  
  def __str__(self) -> str:

    ret_str: str = ""
    current: _Node = self.__head

    while current != None:
      ret_str += str(current.data)
      current = current.next
    
    return ret_str

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
        to_append.data = to_append.data._flip()
        self.__head = to_append
        self.__tail = to_append
        self.__size += 1
        return True
      else:
        return False
    
    if to_append.data.side1 == self.__tail.data.side2:
      self.__tail.next = to_append
      self.__tail = to_append
      to_append.prev = self.__tail
      self.__size += 1
      return True
    elif to_append.data.side2 == self.__tail.data.side2:
      to_append.data = to_append.data._flip()
      self.__tail.next = to_append
      self.__tail = to_append
      to_append.prev = self.__tail
      self.__size += 1
      return True
    else:
      return False
    
  def remove(self, index: int) -> bool:
    """
    Removes the domino at the requested int, and also any dominoes afterwards
    """
    raise NotImplementedError

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
  
  def flip(self) -> None:
    """
    Inverts the order and orientation of dominoes in the chain
    """
    current: _Node = self.__head
    next_node: _Node = None

    while current != None:
      next_node = current.prev
      current.next, current.prev = current.prev, current.next
      current.data = current.data._flip()
      current = next_node

    self.__head, self.__tail = self.__tail, self.__head

class _Node:
  """
  Helper class that holds a domino as data, will be singly linked to the next one.
  """

  def __init__(self, domino: "Domino"):
    self.data: Domino = domino
    self.prev: Optional[_Node] = None
    self.next: Optional[_Node] = None