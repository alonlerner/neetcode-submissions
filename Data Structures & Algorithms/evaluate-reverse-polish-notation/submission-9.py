import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        o = set(['+', '-', '*', '/'])
        for c in tokens:
            if not c in o:
                s.append(int(c))
            else:
                if c == '+':
                    res = s[-2] + s[-1]
                elif c == '-':
                    res = s[-2] - s[-1]
                elif c == '*':
                    res = s[-2] * s[-1]
                else:
                    res = int(s[-2] / s[-1])
                s.pop()
                s.pop()
                s.append(res)
        return s.pop()