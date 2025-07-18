from typing import List

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Time complexity: O(n^2)
# Space complexity: O(1) + O(m) - m = number of triples, n = length of the given array
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # Initiate an empty list to store the results
        nums.sort() # Sort the given List so that we can do the sums easier

        for i, n in enumerate(nums):    # For every index and number (n) in the enumerated list nums - [(0, n), (1, n), (2, n)]
            if i > 0 and n == nums[i - 1]:  # We don't want to use the same value twice
                continue    # Move to the next iteration of the loop

            left, right = i + 1, len(nums) - 1  # Initiate the two pointers, left will be 1 index higher than the first number in our triplet
            while left < right: # Left CAN'T be higher than right
                threeSum = n + nums[left] + nums[right] # The sum of these 3 values should be 0
                if threeSum > 0:    # If the sum is higher than 0 we will move the right pointer to the left
                    right -= 1
                elif threeSum < 0:  # If the sum is lower than 0 we will move the left pointer to the right
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]]) # If the result is 0 we will add the resulting triplets to the results list and move the left pointer to the next value
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:    # If the next value is the same as the previous value for the left pointer, we will move it again
                        left += 1

        return result