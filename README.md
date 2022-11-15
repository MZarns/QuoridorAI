# QuoridorAI

### Description

This project implements four different algorithms for [Quoridor](https://en.wikipedia.org/wiki/Quoridor).

* minimax
* minimax with alpha-beta pruning
* expectimax
* monte carlo tree search

Most of this repo is not my own code. I took an existing quoridor cli game that had broken implementations of the following algorithms. Upgraded and experimented on them. Note, the wall placement mechanism makes for a remarkably high branching factor in the decision trees. I attempt to address this using a variety of strategies. 

### Resources
* [aima-code](https://github.com/aimacode/aima-python)
* [quoridorAgent](https://github.com/dimitrijekaranfilovic/quoridor)

### Running the project

It is recommended that you run this project from a virtual environment.

In order to run the project, you must have [numpy](https://numpy.org/) installed. Navigate to the project root directory and run 

`python3 main.py`.
