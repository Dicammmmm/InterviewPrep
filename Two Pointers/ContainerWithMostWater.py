from typing import List

# You are given an integer array heights where heights[i] represents the height of the ithith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        result = 0  # Initializing the starting result

        for left in range(len(height)): # Iterate through the length of the given list (height)
            for right in range(left + 1, len(height)):  # Right pointer will the left pointer + 1
                # Think of the left pointer as the left pillar and the right as the right pillar
                area = (right - left) * min(height[left], height[right])    # Calculate the area
                result = max(result, area)  # Result is the higher value between the current result and the newly calculated area
            
        return result

# Time complexity: O(n)
# Space complexity: O(1)
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        result = 0  # Our base result is 0 so let's initialzie it
        left, right = 0, len(height) - 1    # We will also initialize our left and right pointers

        while left < right: # We want to loop while the left pointer value is lesser than the right pointer value
            area = (right - left) * min(height[left], height[right])    # This is how we calculate the area of a rectangle, using the minimal height (the bottleneck) as our maximum height
            result = max(result, area)  # The result will be equal to the max value of the current result or the newly calculated area

            if height[left] < height[right]:    # Moving the left pointer after the calculation
                left += 1
            else:
                right -= 1  # Moving the right pointer after the calculation
            
        return result   # Returning the result which is the max area