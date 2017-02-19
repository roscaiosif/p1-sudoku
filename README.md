# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Basically we are adding one more constraint, i.e the naked-twin and an additional elimination step. This could shorten the recursion towards the solution. I added this elimination step after 'reduce_puzzle' returns a valid grid. 

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Adding the two diagonals -'[A1,B2,C3,D4,E5,F6,G7,H8,I9]'and'[A9,B8,C7,D6,E5,F4,G3,H2,I1]' to the unitlist and recalculating the peers, followed by the same procedure of DFS as for the non-diagonal case 


### Code

* `solutions.py`  
* `solution_test.py` 
* `PySudoku.py` 
* `visualize.py` 

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
