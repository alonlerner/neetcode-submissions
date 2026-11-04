# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        temp = slow.next = None
        while second:
            tmp = second.next
            second.next = temp
            temp = second
            second = tmp
        p = head
        second = temp
        while second:
            tmp1 = second.next
            tmp2 = p.next
            p.next = second
            second.next = tmp2
            second = tmp1
            p = tmp2