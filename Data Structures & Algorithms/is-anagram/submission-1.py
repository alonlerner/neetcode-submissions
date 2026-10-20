from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)
        if len(sc) != len(tc):
            return False
        return all(k in tc and sc[k] == tc[k] for k in sc.keys())