class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '[': ']', '{': '}'}
        a = []
        for c in s:
            if c in d:
                a.append(c)
            elif not a or a and c != d[a.pop()]:
                return False
        return not a