from typing import List

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

# SOLUTION 1: Brute Force Approach
# Time complexity: O(n^2) - nested loops iterate through all elements
# Space complexity: O(n) - only for the result array
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Store the length of input array for efficiency
        result = [0] * n  # Initialize result array with zeros, size n

        # Outer loop: iterate through each position i in the array
        for i in range(n):
            prod = 1  # Initialize product accumulator to 1 for each position
            
            # Inner loop: iterate through all positions j to multiply everything except nums[i]
            for j in range(n):
                if i == j:  # Skip the current element at position i
                    continue  # Don't include nums[i] in the product
                prod *= nums[j]  # Multiply current element into the running product
            result[i] = prod  # Store the final product for position i
        return result  # Return the completed result array


# SOLUTION 2: Division-based Approach with Zero Handling
# Time complexity: O(n) - two separate single passes through the array
# Space complexity: O(n) - only for the result array
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0  # Initialize total product and zero counter
        
        # First pass: calculate product of all non-zero elements and count zeros
        for number in nums:
            if number:  # If the number is not zero (truthy check)
                prod *= number  # Multiply it into the total product
            else:  # If the number is zero
                zero_count += 1  # Increment the zero counter
            
        # Special case: if more than one zero exists, all results will be zero
        if zero_count > 1:
            return [0] * len(nums)  # Return array filled with zeros
        
        result = [0] * len(nums)  # Initialize result array with zeros
        
        # Second pass: calculate the result for each position
        for index, count in enumerate(nums):  # Iterate with both index and value
            if zero_count:  # If there's at least one zero in the original array
                # If current element is zero, result is product of all other elements
                # If current element is non-zero, result is 0 (due to zero elsewhere)
                result[index] = 0 if count else prod
            else:  # If no zeros in the original array
                # Divide total product by current element to get product of all others
                result[index] = prod // count  # Use integer division
        return result  # Return the completed result array


# SOLUTION 3: Prefix and Suffix Arrays Approach
# Time complexity: O(n) - three separate passes through the array
# Space complexity: O(n) - additional space for prefix and suffix arrays
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Store array length
        prefix = [0] * n  # Array to store products of elements to the left
        suffix = [0] * n  # Array to store products of elements to the right
        result = [0] * n  # Final result array
        
        # Initialize boundary conditions
        prefix[0] = suffix[n - 1] = 1  # No elements to left of first, no elements to right of last
        
        # First pass: fill prefix array (left to right)
        for i in range(1, n):  # Start from index 1 since prefix[0] is already set
            # prefix[i] = product of all elements to the left of index i
            prefix[i] = nums[i - 1] * prefix[i - 1]  # Previous element * previous prefix product

        # Second pass: fill suffix array (right to left)
        for i in range(n - 2, -1, -1):  # Start from second-to-last element, go backwards
            # suffix[i] = product of all elements to the right of index i
            suffix[i] = nums[i + 1] * suffix[i + 1]  # Next element * next suffix product

        # Third pass: combine prefix and suffix to get final result
        for i in range(n):  # Iterate through all positions
            # Result at position i = (product of left elements) * (product of right elements)
            result[i] = prefix[i] * suffix[i]

        return result  # Return the completed result array


# SOLUTION 4: Space-Optimized Two-Pass Approach
# Time complexity: O(n) - two passes through the array
# Space complexity: O(1) - constant extra space (not counting output array)
class Solution4:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))  # Initialize result array with ones

        # First pass: calculate prefix products and store directly in result array
        prefix = 1  # Running product of elements seen so far from left
        for i in range(len(nums)):  # Iterate left to right
            result[i] = prefix  # Store current prefix product (elements to the left of i)
            prefix *= nums[i]  # Update prefix to include current element for next iteration

        # Second pass: calculate suffix products and multiply with existing prefix values
        suffix = 1  # Running product of elements seen so far from right
        for i in range(len(nums) - 1, -1, -1):  # Iterate right to left
            # Multiply existing prefix product with current suffix product
            result[i] *= suffix  # result[i] now contains prefix[i] * suffix[i]
            suffix *= nums[i]  # Update suffix to include current element for next iteration
        
        return result  # Return the completed result array