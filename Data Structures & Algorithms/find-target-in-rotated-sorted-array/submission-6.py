class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchStart(a, l, r):
            if l >= r:
                return 0
            m = l + (r - l) // 2
            if a[m] > a[m+1]:
                return m + 1
            else:
                if a[l] > a[m]:
                    return searchStart(a, l, m)
                else:
                    return searchStart(a, m+1, r)
        def searchNum(a, l, r, rot, t):
            if l > r:
                return -1
            m = (l + (r - l) // 2 + rot) % len(a)
            if a[m] == t:
                return m
            elif a[m] > t:
                return searchNum(a, l, l + (r - l) // 2 - 1, rot, t)
            else:
                return searchNum(a, l + (r - l) // 2 + 1, r, rot, t)
        r = searchStart(nums, 0, len(nums) - 1)
        return searchNum(nums, 0, len(nums) - 1, r, target)