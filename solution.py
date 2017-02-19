assignments = []


COUNT = 0 # recursionb level

"""
Parameters and functions used for solving the naked-twins problem

"""
ROWS='ABCDEFGHI'
COLS='123456789'

def cross(A, B):
    #"Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

BOXES = cross(ROWS,COLS)
rowunits = [cross(r,COLS) for r in ROWS]
colunits = [cross(ROWS,c) for c in COLS]
squareunits = [cross(rs, cs) for rs in ['ABC','DEF','GHI'] for cs in ['123','456','789']]

UNITLIST = rowunits + colunits + squareunits

def display(values):
    """
    Display the values as a 2-D grid.
    """
    width = 1+ max(len(values[s]) for s in BOXES)
    line = '+'.join(['-'*width*3]*3)
    for r in ROWS:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in COLS))
        if r in 'CF':
            print(line)
    print('\n')

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    twins = [[a for a in u 
                    for b in u 
                        if (a != b) and (len(values[a]) == 2) 
                                    and (values[a] == values[b])
             ] 
             for i,u in enumerate(UNITLIST)
            ]
    # Eliminate the naked twins as possibilities for their units
    for i, twin in enumerate(twins):
        if twin: # if twin is not an empty list
            for box in UNITLIST[i]: 
                if box not in twin: # find the boxes in the unit differnt from those in 'twin'
                    for digit in values[twin[0]]: # for each digit in the values 
                        value = values[box]
                        if len(value) > 1 :
                            value = value.replace(digit,'') # delete the respective digit
                            values[box] = value
    return values

"""
    Class implementation of the sudoku project
"""
class Sudoku():
    """
    Initializing and solving a diagonal or non-diagonal sudoku
    Attributes:
        grid     : initial string value of the sudoku to solve, 81 character long, missing values '.' 
        rows     : string 'ABCDEFGHI'
        cols     : string '123456789'
        boxes    : list of all squares
        unitlist : list of all units 
        peers    : dict of peers for eaach box 
        values   : dict box: digits

    """
    def __init__(self, grid, diag=False, rows='ABCDEFGHI', cols='123456789'):
        """
        Args:
            - grid : 81 charcter long string to be soleved
            - diag :boolean - diagonal sudoku = True 
        Returns:
            all class atributes initialized    

        """
        self.grid = grid
        self.rows = rows
        self.cols = cols
        self.grid_init(diag)

    def cross(self,A, B):
        #"Cross product of elements in A and elements in B."
        return [a+b for a in A for b in B]

    def assign_value(self, box, value):
        """
        Please use this function to update your values dictionary!
        Assigns a value to a given box. If it updates the board record it.
        """
        self.values[box] = value
        if len(value) == 1:
            assignments.append(self.values.copy())

    def grid_init(self, diag):
        """
        Set up the grid and initialize different paramters: 'boxes',  values, 'peers'  for solving
            
        """
        self.boxes = self.cross(self.rows,self.cols)    
        
        self.values = {}
        for box,char in zip(self.boxes,self.grid):
            if char == '.':
                self.values[box] = self.cols
            else:
                self.values[box] = char
 
        rowunits = [self.cross(r,self.cols) for r in self.rows]
        colunits = [self.cross(self.rows,c) for c in self.cols]
        squareunits = [self.cross(rs, cs) for rs in ['ABC','DEF','GHI'] for cs in ['123','456','789']]
        
        self.unitlist = rowunits + colunits + squareunits
        if diag:
            l = len(self.rows)
            self.unitlist.append([self.rows[i]+self.cols[i] for i in range(l)])
            self.unitlist.append([self.rows[i]+self.cols[l-i-1] for i in range(l)])
        
        units = {box:[u for u in self.unitlist if box in u] for box in self.boxes}

        self.peers = {box:set(sum(units[box],[]))-set([box]) for box in self.boxes}

    def display(self):
        """
        Display the values as a 2-D grid.
        """
        width = 1+ max(len(self.values[s]) for s in self.boxes)
        line = '+'.join(['-'*width*3]*3)
        for r in self.rows:
            print(''.join(self.values[r+c].center(width)+('|' if c in '36' else '') for c in self.cols))
            if r in 'CF':
                print(line)
        print('\n')

    def solved_values(self):
        return [box for box in self.boxes if len(self.values[box]) == 1]

    def eliminate(self):
        """
        Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
        """
        solved_values_boxes = self.solved_values()
        for box in solved_values_boxes:
            digit = self.values[box]
            for peer in self.peers[box]:
                value = self.values[peer]
                value = value.replace(digit,'')
                self.assign_value(peer, value)
    
    def only_choice(self):
        """
        Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
        """    
        for unit in self.unitlist:
            for digit in self.cols:
                boxes_containing_digit =[box for box in unit if digit in self.values[box]]
                if len(boxes_containing_digit) == 1:
                    self.assign_value(boxes_containing_digit[0], digit)

    def reduce_puzzle(self):
        """
        Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
        If the sudoku is solved, return the sudoku.
        If after an iteration of both functions, the sudoku remains the same, return the sudoku.
        """      
        stalled = False
        while not stalled:
            solved_values_before = self.solved_values()
            self.eliminate()
            self.only_choice()
            solved_values_after = self.solved_values()

            stalled = solved_values_before == solved_values_after

            if len([box for box in self.boxes if len( self.values[box]) == 0]):
                # if it is still solvable run naked_twins or not
                self.naked_twins()
                return True
        return False
      
    def search(self):
        #"Using depth-first search and propagation, create a search tree and solve the sudoku."
        # First, reduce the puzzle 
        global COUNT # count the recursion level
        COUNT +=1

        failed = self.reduce_puzzle()
        if failed :
            return False # Tree-leaf: not a solution 
        if all(len(self.values[box]) == 1 for box in self.boxes):
            return True # sudoku solved 
       
        # Choose one of the unfilled squares with the fewest possibilities
        n, box = min((len(self.values[box]),box) for box in self.boxes if len(self.values[box]) >1 )

        # Now use recursion to solve each one of the resulting sudokus
        for digit in self.values[box]:
            tmp = self.values.copy() # copy of the values in case of failure = 'attempt ===False'
            self.values[box] = digit
            attempt = self.search()
            if attempt:
                return attempt
            else:
                self.values = tmp
            
    def naked_twins(self):
        """Eliminate values using the naked twins strategy.
        Args:
            values(dict): a dictionary of the form {'box_name': '123456789', ...}

        Returns:
            the values dictionary with the naked twins eliminated from peers.
        """
        # Find all instances of naked twins
        twins = [[a for a in u 
                        for b in u 
                            if (a != b) and (len(self.values[a]) == 2) 
                                        and (self.values[a] == self.values[b])
                 ] 
                 for i,u in enumerate(self.unitlist)
                ]
        # Eliminate the naked twins as possibilities for their units
        for i, twin in enumerate(twins):
            if twin:
                for box in self.unitlist[i]: 
                    if box not in twin:
                        for digit in self.values[twin[0]]:
                            value = self.values[box]
                            if len(value) > 1 :
                                value = value.replace(digit,'')
                                self.assign_value(box, value)


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    diagonal_sudoku = Sudoku(grid, diag=True)
    diagonal_sudoku.search()
    diagonal_sudoku.display()
    
    return  diagonal_sudoku.values
 

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
 
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
