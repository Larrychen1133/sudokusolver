# Sudoku Solver

This Python program tackles the classic 9x9 Sudoku puzzle with an efficient algorithmic approach. It employs backtracking search with the minimum remaining value (MRV) heuristic and incorporates forward checking to prune the search space and speed up the solving process.

## Features

- Solves any 9x9 Sudoku puzzle.
- Utilizes backtracking search for the core algorithm.
- Applies the MRV heuristic to choose the next variable to assign.
- Implements forward checking to reduce the domains of future variables, thereby pruning the search space.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Before running this program, ensure you have Python 3 installed on your system. You can download Python 3 from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine using the following command:

git clone https://github.com/Larrychen1133/sudoku-solver.git


2. Change into the project directory:

cd sudoku-solver


### Usage

To solve a Sudoku puzzle, run the program from the command line, passing the Sudoku puzzle as a single string argument where '0' represents an empty cell. For example:

python3 sudoku.py "003020600900305001001806400008102900700000008006708200002609500800203009005010300"



This string represents the following Sudoku board:
|   |   | 3 |   | 2 |   | 6 |   |   |
|---|---|---|---|---|---|---|---|---|
| 9 |   |   | 3 |   | 5 |   |   | 1 |
|   |   | 1 | 8 |   | 6 | 4 |   |   |
|   |   | 8 | 1 |   | 2 | 9 |   |   |
| 7 |   |   |   |   |   |   |   | 8 |
|   |   | 6 | 7 |   | 8 | 2 |   |   |
|   |   | 2 | 6 |   | 9 | 5 |   |   |
| 8 |   |   | 2 |   | 3 |   |   | 9 |
|   |   | 5 |   | 1 |   | 3 |   |   |




Upon successful execution, the program will output the solved Sudoku puzzle.
