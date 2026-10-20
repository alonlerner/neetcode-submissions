import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqCount = Counter(nums)
        freqNumCount = {}
        for key in numFreqCount.keys():
            if numFreqCount[key] in freqNumCount:
                freqNumCount[numFreqCount[key]].append(key)
            else:
                freqNumCount[numFreqCount[key]] = [key]
        LargestFreq = heapq.nlargest(k, numFreqCount.values())
        output = []
        for freq in LargestFreq:
            output.append(freqNumCount[freq].pop())
        return output