# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nn = head.next
        head.next = None
        while nn:
            temp = nn.next
            nn.next = head
            head = nn
            nn = temp
        return head