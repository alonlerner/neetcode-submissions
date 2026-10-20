# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memAddSet = set()
        while head:
            if id(head) in memAddSet:
                return True
            memAddSet.add(id(head))
            head = head.next
        return False