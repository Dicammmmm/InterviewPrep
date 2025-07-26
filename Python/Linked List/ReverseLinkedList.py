from typing import Optional

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
class Solution1:
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        previous, current = None, head
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        return previous

# Time complexity: O(n)
# Space complexity: O(n)
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead