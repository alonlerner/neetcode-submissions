from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterMap = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for n in counterMap:
            freq[counterMap[n]].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res