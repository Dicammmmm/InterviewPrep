from typing import List

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Time complexity: O(n)
# Space complexity: O(n)
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = [] # Initialize an empty stack, we'll store opening brackets as we encounter them
        # Initialize a hashmap which will contain the closing parenthesis and their open equivalvents
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
            }
        
        for char in s:  # We will examine every character in the string
            if char in closeToOpen: # Check if it is a closing bracket
                if stack and stack[-1] == closeToOpen[char]: # We want to make sure that our stack is not empty and we want to make sure that the top value of the stack is a matching parenthesis
                    stack.pop() # Pop from the stack if they match
                else:
                    return False    # Our parenthesis don't match
            else:
                stack.append(char)  # If the character is NOT a closing bracket, then it is an opening bracket so let's store it in the stack
        
        return True if not stack else False # Return true ONLY if our stack is empty

# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution2:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:  # We can brute force the issue by replacing every open and closed parenthesis with an empty string
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''  # After manipluating the string, if all we are left is an empty string then we will get true and if not we will get false