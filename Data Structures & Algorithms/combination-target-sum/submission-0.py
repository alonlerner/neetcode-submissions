class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        combsSum = []
        res = []
        for num in nums:
            if num == target:
                res.append([num])
            elif num < target:
                combs.append([num])
                combsSum.append(num)
            i = 0
            while i < len(combs):
                if combsSum[i] + num == target:
                    res.append(combs[i] + [num])
                elif combsSum[i] + num < target:
                    combs.append(combs[i] + [num])
                    combsSum.append(combsSum[i] + num)
                i += 1
        return res