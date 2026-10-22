class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) <= n:
            res += [res[i] + 1 for i in range(len(res)) if i + len(res) <= n]
        return res