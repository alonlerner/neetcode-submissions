class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0] * (n + 1)
        a[0] = 1
        for i in range(n):
            if i + 1 <= n:
                a[i+1] += a[i]
            if i + 2 <= n:
                a[i+2] += a[i]
        return a[-1]