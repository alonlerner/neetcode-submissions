import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [[lists[i].val, i] for i in range(len(lists)) if lists[i]]
        heapq.heapify(h)
        dummy = ListNode()
        p = dummy
        while h:
            pop = heapq.heappop(h)
            p.next = lists[pop[1]]
            p = p.next
            lists[pop[1]] = lists[pop[1]].next
            if lists[pop[1]]:
                heapq.heappush(h, [lists[pop[1]].val, pop[1]])
        return dummy.next