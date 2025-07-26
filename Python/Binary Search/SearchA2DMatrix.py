from typing import List

# You are given an m x n 2-D integer array matrix and an integer target.
#     Each row in matrix is sorted in non-decreasing order.
#     The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.
# Can you write a solution that runs in O(log(m * n)) time?

# Time complexity: O(log⁡(m ∗ n)) - m = number of rows, n = number of columns
# Space complexity: O(1)
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0]) # Length of the matrix is the total number of rows, while length of the 1st row is the number of columns
        top, bot = 0, rows - 1  # Top row is 0, and the bottom row is the length of the matrix -1

        while top <= bot:   # While the top row is smaller or equal to the bottom row we want to get the middle row
            row = (top + bot) // 2  # This is how we find the target row
            if target > matrix[row][-1]:    # If the target is greater than the max value of the row then we move the top row down
                top = row + 1
            elif target < matrix[row][0]:  # If the target value is smaller than the min value of the row then we move the bottom row up
                bot = row - 1
            else:
                break   # If we found the row that corresponds to our target, we will break from the loop
        
        if not (top <= bot): # If we can't find the row that corresponds to our target we will return False
            return False
        
        row = (top + bot) // 2  # We will find our target row
        left, right = 0, cols - 1   # Initialize the left and right pointer

        while left <= right:    # While the left pointer is smaller or equal to the right pointer
            mid = (left + right) // 2   # We want to find the middle value
            if target > matrix[row][mid]:   # If the target is greater than the middle value then we will move the left pointer to the right
                left = mid + 1
            elif target < matrix[row][mid]: # If the target value is smaller than the middle value then we will move the right pointer to the left
                right = mid - 1
            else:
                return True # If we found the result we will return True
        
        return False    # If after all the checks we haven't found the result then the result doesn't exist in the given matrix

# Time complexity: O(m * n) - m = number of rows, n = number of columns
# Space complexity: O(1)
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):  # For every row in the matrix
            for number in range(len(matrix[0])):    # Check every number in the matrix
                if matrix[row][number] == target:   # If number in the matrix is the target
                    return True # Return True
        
        return False    # If the target is not found, return False

# Time complexity: O(m + n) - m = number of rows, n = number of columns
# Space complexity: O(1)
class Soltuion3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])   # Rows is the length of the matrix, number of columns is the length of the first list in the matrix
        row, column = 0, columns - 1    # Starting row is 0, starting column is the last in the list

        while row < rows and column >= 0:   # While the row number is smaller than the total number of rows and column is higher or equal to 0 (the first entry of the list)
            if matrix[row][column] > target:    # Check if the value is greater than the target
                column -= 1 # If it is, move the column backwards to a smaller value
            elif matrix[row][column] < target:  # Check if the value is smaller than the target
                row += 1    # If it is, move the row down
            else:
                return True # If the value is equal to the target return True
        return False    # IF the target value cannot be found return False

# Time complexity: O(log(m * n)) - m = number of rows, n = number of columns
# Space complexity: O(1)
class Solution4:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0]) # Rows is the length of the matrix, number of columns is the length of the first list in the matrix
        left, right = 0, rows * columns -1  # Left pointer is at 0 and the right pointer is at the last element in the matrix

        while left <= right:
            mid = left + (right - left) // 2   # Find the middle value
            row, column = mid // columns, mid % columns # Convert 1D index back to 2D index
            if target > matrix[row][column]:    # Target is in the right half
                left = mid + 1
            elif target < matrix[row][column]:  # Target is in the left half
                right = mid - 1
            else:
                return True # Target found
        
        return False    # Target not found