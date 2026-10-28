class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m+1] > nums[r]:
                l = m + 1
            else:
                r = m