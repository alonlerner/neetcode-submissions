class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = [-1] * 101
        o = []
        for i in range(len(temperatures) - 1, -1, -1):
            o.append(a[temperatures[i]] - i if a[temperatures[i]] - i > 0 else 0)
            for j in range(temperatures[i]):
                a[j] = i
        return o[::-1]