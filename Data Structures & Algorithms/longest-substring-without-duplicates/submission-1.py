class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ls = 0, 0, 0
        charInd = {}
        while j < len(s):
            if s[j] in charInd and charInd[s[j]] >= i:
                i = charInd[s[j]] + 1
            else:
                ls = max(ls, j - i + 1)
            charInd[s[j]] = j
            j += 1
        return ls
