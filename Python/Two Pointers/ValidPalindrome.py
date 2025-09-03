# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Time complexity: O(n)
# Space complexity: O(1)
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 # Initialize pointers: left at start, right at end

        while left < right:  # Continue until pointers meet

            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from the right  
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1
        
        return True  # All characters matched

# Time complexity: O(n)
# Space complexity: O(n)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        newS = ''   # Initialize a new empty string

        for c in s:                 # For every character in the string
            if c.isalnum():         # Check if it's alphanumeric
                newS += c.lower()   # Add the character to the string in a lower case
            
        return newS == newS[::-1]   # Check if it's a palindrome