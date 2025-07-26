import bisect
from typing import List

# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn)O(logn) time.

# Time complexity: O(log n)
# Space complexity: O(1)
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Initialize pointers at start and end of array

        while left <= right:    # Continue while the search space is valid
            mid = (left + right) // 2   # Find midpoint to eliminate half the search space
            # NOTE: Some programming languages might have issues with overflow if the list is to big,
            #  so we can use mid = left + (right - left) // 2 to avoid overflow
            
            if nums[mid] > target:      # If target is less than mid value, search left half
                right = mid - 1         # Move right pointer left of midpoint
            elif nums[mid] < target:    # If target is greater than mid value, search right half
                left = mid + 1          # Move left pointer right of midpoint
            else:
                return mid              # Found target, return its index
        
        return -1   # Target not found in array

# Time complexity: O(log n)
# Space complexity: O(log n)
class Solution2:
    def binary_search(self, left: int, right: int, nums: List[int], target: int) -> int:
        if left > right:  # Base case: search space is invalid
            return -1
        mid = left + (right - left) // 2  # Calculate midpoint safely

        if nums[mid] == target:  # If mid value is target, return index
            return mid
        if nums[mid] < target:   # If mid value is less than target, search right half
            return self.binary_search(mid + 1, right, nums, target)
        return self.binary_search(left, mid - 1, nums, target)  # Otherwise, search left half

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)  # Start recursive search

# Time complexity: O(log n)
# Space complexity: O(1)
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # Initialize pointers for search space

        while left < right:  # Continue while search space is valid
            mid = left + ((right - left) // 2)  # Calculate midpoint safely
            if nums[mid] > target:  # If mid value is greater than target, search left half
                right = mid         # Move right pointer to mid
            elif nums[mid] <= target:  # If mid value is less than or equal to target, search right half
                left = mid + 1        # Move left pointer right of mid
        # After loop, check if target is at left-1
        return left - 1 if (left and nums[left - 1] == target) else -1

# Time complexity: O(log n)
# Space complexity: O(1)
class Solution4:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # Initialize pointers for search space

        while left < right:  # Continue while search space is valid
            mid = left + ((right - left) // 2)  # Calculate midpoint safely
            if nums[mid] >= target:  # If mid value is greater than or equal to target, search left half
                right = mid          # Move right pointer to mid
            elif nums[mid] < target:  # If mid value is less than target, search right half
                left = mid + 1       # Move left pointer right of mid
        # After loop, check if target is at left
        return left if (left < len(nums) and nums[left] == target) else -1

# Time complexity: O(log n)
# Space complexity: O(1)
class Solution5:
    def search(self, nums: List[int], target: int) -> int:
        # Find the leftmost index to insert target in nums to keep it sorted
        index = bisect.bisect_left(nums, target)
        # Check if the target exists at the found index; return index if found, else -1
        return index if index < len(nums) and nums[index] == target else -1