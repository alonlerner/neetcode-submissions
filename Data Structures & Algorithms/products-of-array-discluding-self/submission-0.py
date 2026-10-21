class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = nums.copy()
        rm = nums.copy()
        res = []
        for i in range(1, len(nums)):
            lm[i] *= lm[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rm[i] *= rm[i+1]
        for i in range(len(nums)):
            res.append((lm[i-1] if i > 0 else 1) * (rm[i+1] if i < len(nums) - 1 else 1))
        return res