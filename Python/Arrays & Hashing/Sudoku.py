from typing import List
from collections import defaultdict

# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
#     Each row must contain the digits 1-9 without duplicates.
#     Each column must contain the digits 1-9 without duplicates.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check every row in the board for duplicates
        for row in range(9):                # For each row in the range of 9, which is the size of the board
            seen = set()                    # Create a set which will track the numbers we have seen
            for i in range(9):              # Create a pointer to check each value in the row
                if board[row][i] == ".":    # If the value is empty, presented as a dot, skip it
                    continue
                if board[row][i] in seen:   # If the value is already in the set then the board is invalid
                    return False
                seen.add(board[row][i])     # If the value is not in the set, we add it
        
        # Check every column if it's valid
        for col in range(9):                # For each column in the range of 9, which is the size of the board
            seen = set()                    # Create a set which will track the numbers we have seen
            for i in range(9):              # Create a pointer to check each value in the column
                if board[i][col] == ".":    # If the value is empty, present as a dot, skip it
                    continue
                if board[i][col] in seen:   # If the value is already in the set then the board is invalid
                    return False
                seen.add(board[i][col])     # If the value is not in the set, we add it
        
        # Check every 3x3 square if it's valid
        for square in range(9):                 # For each square in the range of 9, which is how many squares there are
            seen = set()                        # Create a set which will track the numbers we have seen
            for i in range(3):                  # Create a pointer to check each value in the row
                for j in range(3):              # Create a point to check each value in the column
                    row = (square // 3) * 3 + i # Get the row value
                    col = (square % 3) * 3 + j  # Get the column value
                    if board[row][col] == ".":  # If the value is empty, presented by a dot, skip it
                        continue
                    if board[row][col] in seen: # If the value is already in the set then the board is invalid
                        return False
                    seen.add(board[row][col])   # If the value is not in the set, we add it
        
        return True # If the sudoku board is valid, we return true

# Time complexity: O(n^2)
# Space complexity: O(n^2)
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)     # Key is column number, value is a set which represents all values in the column
        rows = defaultdict(set)     # Key is the row number, value is a set which represents all values in the row
        squares = defaultdict(set)  # key is a tuple (row//3, col//3) representing which 3x3 square the cell belongs to

        # We check every row and column in the sudoku board
        for row in range(9):                # Sudoku board has 9 rows so we use range 9
            for col in range(9):            # Sudoku board has 9 column so we use range 9
                if board[row][col] == ".":  # If the vlaue in the specific spot is empty, represented by a dot, we move to the next value
                    continue
                
                # We check if we have already seen this value in the current row, column, or 3x3 square
                if (board[row][col] in rows[row]                            # We check if we have seen the value in any of the rows
                    or board[row][col] in cols[col]                         # We check if we have seen the value in any of the columns
                    or board[row][col] in squares[(row // 3), (col // 3)]): # We check if we have seen the value in the current 3x3 square
                        return False    # If we have, we return false
                
                cols[col].add(board[row][col])                          # If we haven't, we add the value to the columns set
                rows[row].add(board[row][col])                          # If we haven't, we add the value to the rows set
                squares[(row // 3), (col // 3)].add(board[row][col])    # If we haven't seen the value in the current square, we add it to the square set
        
        return True # If the sudoku board is valid, we return true

# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution3:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Instead of sets, we use integers as bitmasks to track seen digits
        # Each bit position represents a digit (bit 0 = digit 1, bit 1 = digit 2, etc.)
        rows = [0] * 9      # Array of 9 integers, each tracks seen digits for that row using bits
        cols = [0] * 9      # Array of 9 integers, each tracks seen digits for that column using bits  
        squares = [0] * 9   # Array of 9 integers, each tracks seen digits for that 3x3 square using bits

        for row in range(9):                # For each row in the 9x9 sudoku board
            for col in range(9):            # For each column in the 9x9 sudoku board
                if board[row][col] == ".":  # If the value in the current cell is empty, represented by a dot, skip it
                    continue
                
                # Convert the digit character to a zero-based index (digit 1 becomes index 0, digit 9 becomes index 8)
                value = int(board[row][col]) - 1
                
                # Check if we've already seen this digit in the current row
                # (1 << value) creates a bitmask with only the bit for this digit set
                # & operator checks if that bit is already set in rows[row]
                if (1 << value) & rows[row]:
                    return False    # Duplicate found in row, sudoku is invalid
                
                # Check if we've already seen this digit in the current column
                # Same logic as above but checking the column bitmask
                if (1 << value) & cols[col]:
                    return False    # Duplicate found in column, sudoku is invalid
                
                # Check if we've already seen this digit in the current 3x3 square
                # (row // 3) * 3 + (col // 3) converts 2D square position to 1D index (0-8)
                if (1 << value) & squares[(row // 3) * 3 + (col // 3)]:
                    return False    # Duplicate found in 3x3 square, sudoku is invalid
                
                # Mark this digit as seen by setting the corresponding bit
                # |= operator performs bitwise OR and assigns the result back
                rows[row] |= (1 << value)                               # Set the bit for this digit in the row bitmask
                cols[col] |= (1 << value)                               # Set the bit for this digit in the column bitmask  
                squares[(row // 3) * 3 + (col // 3)] |= (1 << value)    # Set the bit for this digit in the 3x3 square bitmask
            
        return True # If no duplicates found after checking all cells, the sudoku board is valid