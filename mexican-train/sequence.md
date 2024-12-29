# Mexican Train

The "solve" in mexican train dominoes comes down to creating a sequence of dominos as long as possible. This isn't a rule in the official game, but as a house rule the first turn begins by building out the longest possible "train" by matching one side of the domino to the spinner, then attaching new ones turn by turn with the same rules.

A player will begin the game with **13 dominoes** unless they have that round's spinner, in which case they start with 12.

## The Goal

Given a sequence of dominoes, create the longest possible chain with some additional stipulations.

1. Ties in chain length should be broken by **point value** calculated by summing the number of pips on each one.

2. If there are multiple dominoes which could be used next to the spinner (start the chain), those should be kept as "mulligan" pieces since they can be played for free on your turn.

3. Any double must immediately be followed by a valid domino, therefore the last domino in the chain cannot be a double.

4. All of the above rules are **ignored** if the chain uses the entire hand, as this is an instant win.
