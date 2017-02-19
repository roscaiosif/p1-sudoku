# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A:  Constraint propagation works by reducing domains of variables, strengthening constraints, or creating new ones*. This leads to a reduction of the search space, making the problem easier to solve by some algorithms. Naked-twins are occurences of two-digit values in the same  unit (row, column, square or diagonal). In fact this ensures that those digits will be distributed between the two occurences, therefore the same digits can be removed form the other members of the unit. Basically we are adding one more constraint that allows additional reduction of the possible digits. This in fact could shorten the recursion towards the solution. I added this elimination step after `reduce_puzzle` returns a valid grid. 

*https://en.wikipedia.org/wiki/Local_consistency

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In order to solve a diagonal sudoku an additiopnal constraint is needed. Adding the two diagonals -'[A1,B2,C3,D4,E5,F6,G7,H8,I9]'and'[A9,B8,C7,D6,E5,F4,G3,H2,I1]' to the `unitlist` and considering these for establishing the peers, will constitute the necessary constraint which combined by the DFS procedure will produce possible solution to the diagonal sudoku problem 


### Code

* `solutions.py`  
* `solution_test.py` 
* `PySudoku.py` 
* `visualize.py` 

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
