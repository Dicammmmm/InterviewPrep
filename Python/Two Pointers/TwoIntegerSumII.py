from typing import List

# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.
# Your solution must use O(1)O(1) additional space.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution1:
    def twoSum(self, numbers : List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 # Initialize the left and the right pointers

        while left < right: # While the left pointer is behind the right pointer
            res = numbers[left] + numbers[right]   # What is the current sum?

            if res == target:  # If we found the target 
                return [left + 1, right + 1]    # Return the indexes +1
            
            elif res < target:  # If the target is larger than the result, move the left pointer to the right
                left += 1
            else:
                right -= 1  # If the target is smaller than the result, move the right pointer to the left
        
        return []