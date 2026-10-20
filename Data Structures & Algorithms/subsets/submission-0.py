class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            b = len(res)
            for j in range(b):
                res.append(res[j] + [nums[i]])
        return res