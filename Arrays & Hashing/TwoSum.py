from typing import List

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Time complexity: O(n)
# Space complexity: O(n)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}    # Initiate an empty hash map

        for i, n in enumerate(nums):    # For every index, number in enumerated list of nums
            diff = target - n           # Calculate the complement we need to find
            if diff in map:             # If the complement is in the map, return both indices
                return [map[diff], i]
            
            map[n] = i                  # Store current number with its index for future lookups
        raise ValueError() # No solution found
        
# Time complexity: O(n log n)
# Space complexity: O(n)
class Solution2:
    def twoSum(self, nums: List[list], target: int) -> List[int]:
        A = []                          # Initiate an empty list
        for i, num in enumerate(nums):  # For every index, number in enumerated list of nums
            A.append([num, i])          # Create a a Value-Index pair
        
        A.sort()                        # Sort by the first element (the value)
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]     # Sum of values at left and right pointers
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            
            elif cur < target:
                i += 1                  # Need larger sum, move left pointer right
            else:
                j -= 1                  # Need smaller sum, move right pointer left
        
        return []