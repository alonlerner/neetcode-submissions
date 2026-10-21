import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        heap = []
        res = []
        for i in range(len(points)):
            dist = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heap.append(dist)
            if dist in d:
                d[dist].append(points[i])
            else:
                d[dist] = [points[i]]
        heapq.heapify(heap)
        for i in range(k):
            pop = heapq.heappop(heap)
            res.append(d[pop].pop())
        return res