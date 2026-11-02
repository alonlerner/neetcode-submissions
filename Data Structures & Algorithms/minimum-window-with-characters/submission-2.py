from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        window = defaultdict(int)
        res = [0, 0]
        minLen = float('inf')
        l = 0
        have, need = 0, len(counter.values())
        for i in range(len(s)):
            if s[i] in counter:
                window[s[i]] += 1
                if window[s[i]] == counter[s[i]]:
                    have += 1
                    if need == have:
                        while need == have:
                            if i - l + 1 < minLen:
                                minLen = i - l + 1
                                res = [l, i+1]
                            window[s[l]] -= 1
                            if s[l] in counter and window[s[l]] < counter[s[l]]:
                                have -= 1
                            l += 1
        return s[res[0]:res[1]]