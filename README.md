# QuoridorAI

## Description

This project implements four AI algorithms for [Quoridor](https://en.wikipedia.org/wiki/Quoridor).

* Minimax
* Minimax with Alpha-Beta Pruning
* Expectimax
* Monte Carlo Tree Search

### Resources

* [aima-code](https://github.com/aimacode/aima-python)
* [quoridorAgent](https://github.com/dimitrijekaranfilovic/quoridor)

### Running the project

* Install [numpy](https://numpy.org/)
* Navigate to the project root directory and run `python3 main.py`

Note: the wall placement mechanism makes for a remarkably high branching factor in the decision trees. I address this by applying a manual heuristic to prioritize wall placements immediately adjacent to existing walls and pawns, mimicking human tendencies.
