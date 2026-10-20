# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        pointer = dummy
        while l1 and l2:
            nodeSum = l1.val + l2.val + carry
            pointer.next = ListNode(nodeSum % 10)
            carry = nodeSum // 10
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            nodeSum = l1.val + carry
            pointer.next = ListNode(nodeSum % 10)
            carry = nodeSum // 10
            pointer = pointer.next
            l1 = l1.next
        while l2:
            nodeSum = l2.val + carry
            pointer.next = ListNode(nodeSum % 10)
            carry = nodeSum // 10
            pointer = pointer.next
            l2 = l2.next
        if carry:
            pointer.next = ListNode(1)
        return dummy.next