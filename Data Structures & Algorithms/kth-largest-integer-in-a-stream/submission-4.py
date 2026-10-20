import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.a = nums
        heapq.heapify(self.a)
        while len(self.a) > k:
            heapq.heappop(self.a)

    def add(self, val: int) -> int:
        if self.a and val <= self.a[0]:
            return self.a[0]
        if self.a and len(self.a) == self.k:
            heapq.heappop(self.a)
        heapq.heappush(self.a, val)
        return self.a[0]
