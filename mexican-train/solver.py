from helpers.chain import *
from helpers.domino import *
from typing import Optional

class Solver:
  """
  The Solver class should be able to take an array of dominos and
  work out the 'best' possible sequence given them.
  """
  def __init__(self, spinner: int=12) -> None:
    self.hand: list["Domino"] = []
    self.size: int = 0
    self.spinner: int = spinner

  def add_domino(self, dom1: int, dom2: int) -> None:
    self.hand.append(Domino(dom1, dom2))
    self.size += 1
  
  def set_spinner(self, spinner: int) -> None:
    if 0 <= spinner <= 12:
      raise ValueError 
  
  def remove_domino(self, dom: Domino) -> bool:
    if dom in self.hand:
      self.hand.remove(dom)
      self.size -= 1
      return True
    return False
    

  def solve(self) -> Chain:
    """
    Creates and returns the longest possible chain using the current dominos in hand.
    
    Solved first with a simple DFS approach to return the longest possible chain,
    with any ties in length being broken by score of the chain.
    """

    starters: list[Domino] = []
    edges: list = []
    num_dominoes: int = self.size
    adjacency: dict[Domino, list[Domino]] = {domino: [] for domino in self.hand}
    adjacency.update({domino._flip(): [] for domino in self.hand})

    ret_chain: Optional[Chain] = None

    # Get possible domino chain starters.
    for domino in self.hand:
      if domino.side1 == self.spinner:
        starters.append(domino)
      elif domino.side2 == self.spinner:
        starters.append(domino._flip())

    # Create possible edges
    for i in range(num_dominoes):
      for j in range(i, num_dominoes):
        if self.hand[i].can_connect(self.hand[j]):
          edges.append([self.hand[i], self.hand[j]])
        elif self.hand[i].can_connect(self.hand[j]._flip()):
          edges.append([self.hand[i], self.hand[j]._flip()])
        elif self.hand[i]._flip().can_connect(self.hand[j]._flip()):
          edges.append(self.hand[i]._flip(), self.hand[j]._flip())
        elif self.hand[i]._flip().can_connect(self.hand[j]):
          edges.append(self.hand[i]._flip(), self.hand[j])
    
    # Populate adjacency list
    for e in edges:
      adjacency[e[0]].append(e[1])
    
    # Perform DFS on every starter domino
    
    
        


    

    
    


  