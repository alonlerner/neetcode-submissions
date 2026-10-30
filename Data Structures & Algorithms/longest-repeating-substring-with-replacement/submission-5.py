from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, r = 0, 1
        longest = 1
        counts[s[l]] = 1
        while r < len(s):
            counts[s[r]] += 1
            common = max(counts.values())
            if r - l + 1 - common > k:
                counts[s[l]] -= 1
                l += 1
            else:
                longest = max(longest, r - l + 1)
            r += 1
        return longest