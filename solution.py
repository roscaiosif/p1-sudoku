import sudoku as sdk

def test_naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    sudoku = sdk.Sudoku(values,partial=True)
    sudoku.naked_twins()
 
    return sudoku.values

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    diagonal_sudoku = sdk.Sudoku(grid, diag=True)
    diagonal_sudoku.search()
    diagonal_sudoku.display()
    
    return  diagonal_sudoku.values
 
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    solve(diag_sudoku_grid)
 
    try:
        from visualize import visualize_assignments
        visualize_assignments(sdk.assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
