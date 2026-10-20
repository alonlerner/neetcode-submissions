import math
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def findElement(nums, t, l, r):
            if l > r:
                return False
            m = math.floor(l / 2 + r / 2)
            if nums[m] == t:
                return m
            elif nums[m] > t:
                return findElement(nums, t, l, m - 1)
            else:
                return findElement(nums, t, m + 1, r)
        i, j = 0, 0
        for i in range(len(numbers) - 1):
            rv = findElement(numbers, target - numbers[i], i + 1, len(numbers) - 1)
            if rv:
                return [i+1, rv+1]
        return [-1, -1]