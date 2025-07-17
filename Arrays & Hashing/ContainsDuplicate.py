from typing import List

 # Given an integer array nums, return true if any value appears at least twice in the array, 
 # and return false if every element is distinct.

# Time complexity: O(n)
# Space complexity: O(n)
class Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()        # Initialize an empty set
        # Sets can't contain duplicate values, perfect for this use case

        for num in nums:    # For every number in the nums list
            if num in seen: # Check if the number has been seen before
                return True # If the number has been seen, then it is a duplicate
            seen.add(num)   # Add the number to the set
       
        return False        # No duplicates found after checking all numbers

# Time complexity: O(n log n)
# Space complexity: O(1)
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # Sorting the list so that all duplicate numbers are adjacent

        for i in range(1, len(nums)):   # Checking every index in the range of 1 to the length of the list
            if nums[i] == nums[i - 1]:  # if the value of the index i is equal to the value of the previous index return True
                return True
            
        return False

# Time complexity: O(n)
# Space complexity: O(n)
class Solution3:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len (nums) # Return true if the set of nums is smaller than the list of nums, sets automatically remove duplicates