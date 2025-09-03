from typing import List

# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Time complexity: O(4^n / √n)
# Space complexity: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []      # Stores current combination being built
        result = []     # Stores all valid combinations
        
        def backtrack(openN, closedN):
            # openN = count of open parens added so far
            # closedN = count of closed parens added so far
            
            if openN == closedN == n:
                # Base case: we have n opens and n closes
                result.append("".join(stack))
                return
            
            if openN < n:
                # Can still add opening parenthesis
                stack.append("(")               # Add "(" to current combination
                backtrack(openN + 1, closedN)   # Recursively explore
                stack.pop()                     # BACKTRACK - remove "("
            
            if closedN < openN:
                # Can add closing parenthesis (must have matching open)
                stack.append(")")               # Add ")" to current combination  
                backtrack(openN, closedN + 1)   # Recursively explore
                stack.pop()                     # BACKTRACK - remove ")"
            
        backtrack(0, 0)    # Start with 0 opens, 0 closes
        return result