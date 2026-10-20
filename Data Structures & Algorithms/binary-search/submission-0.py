class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while j > i:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        return -1