from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createCounterTuple(s):
            charCounter = [0] * 26
            for c in s:
                charCounter[ord(c) - ord('a')] += 1
            return tuple(charCounter)
        counterToIndDict = {}
        o = []
        for i in range(len(strs)):
            strCounter = createCounterTuple(strs[i])
            if strCounter in counterToIndDict:
                o[counterToIndDict[strCounter]].append(strs[i])
            else:
                counterToIndDict[strCounter] = len(o)
                o.append([strs[i]])
        return o