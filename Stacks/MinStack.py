# Design a stack class that supports the push, pop, top, and getMin operations.
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1)O(1) time.

# Time complexity: O(1) - for all operations
# Space complexity: O(n)
class Solution1:
    def __init__(self) -> None:
        self.stack = []     # Initialize main stack
        self.minStack = []  # Initialize stack to track minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)  # Add value to main stack
        # Find minimum between current value and current stack minimum
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)   # Add minimum to minStack

    def pop(self) -> None:
        self.stack.pop()    # Remove from main stack
        self.minStack.pop() # Remove corresponding minimum

    def top(self) -> int:
        return self.stack[-1]   # Return top element of main stack

    def getMin(self) -> int:
        return self.minStack[-1]    # Return current minimum