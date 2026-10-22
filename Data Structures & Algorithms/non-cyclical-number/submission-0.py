class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while not n in s and n != 1:
            s.add(n)
            temp = 0
            while n != 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp
        return True if n == 1 else False