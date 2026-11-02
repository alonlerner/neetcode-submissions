# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        l = 0
        while p:
            l += 1
            p = p.next
        if l - n == 0:
            return head.next
        p = head
        for i in range(l-n-1):
            p = p.next
        p.next = p.next.next
        return head