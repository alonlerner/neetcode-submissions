class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l1, l2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            l1, l2 = l2, min(l1, l2) + cost[i]
            print(l1, l2)
        return min(l1, l2)