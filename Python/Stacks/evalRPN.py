# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.

# Time complexity: O(n)
# Space complexity: O(n)
class Solution1:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []  # Initialize an empty stack

        for t in tokens:    # Do this for every token in the tokens list
            if t == "+":    # If the token is a plus operator do the following
                stack.append(stack.pop() + stack.pop()) # Append to the stack the sum of the two previous values and pop them, leaving us only with the result 
            elif t == "-":
                x, y = stack.pop(), stack.pop() # We want to get the popped values into a placeholder variables
                stack.append(y - x) # Append to the stack the value of y - x.
                # We are doing the subtraction in reverse order as x is the top element (second operand), y is below it (first operand) in the stack and stacks follow last in first out philosophy
            elif t == "*":
                stack.append(stack.pop() * stack.pop()) # Append to the stack the product of the two previous values and pop them, leaving us only with the result in the stack
            elif t == "/":
                x, y = stack.pop(), stack.pop() # We want to get the popped values into a placeholder variables
                stack.append(int(y / x)) # Append to the stack the result of the division and turn it into an integer as this will truncate towards zero
                # We are doing the division in reverse order as x is the top element (second operand), y is below it (first operand) in the stack and stacks follow last in first out philosophy
            else:
                stack.append(int(t))    # If it is not an operator, convert the token to an integer and add it to the stack
            
        return stack[0] # Return the evaluation from the stack

# This code can be improved by using match/case instead of if/else
# We can also add another if statement so that if the token is a letter it would return a ValueError and continue the iteration