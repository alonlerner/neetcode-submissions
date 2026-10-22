class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = 1
        i = len(digits) - 1
        while i >= 0 and r != 0:
            s = digits[i] + r
            digits[i] = s % 10
            r = s // 10
            i -= 1
        if r:
            digits.insert(0, 1)
        return digits