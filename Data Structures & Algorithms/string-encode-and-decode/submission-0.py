class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(strs[i])) + ',' for i in range(len(strs))]
        lengths.append('#')
        return ''.join(lengths) + ''.join(strs)
    def decode(self, s: str) -> List[str]:
        ht = s.index('#')
        i, j = 0, ht + 1
        strs = []
        nextComma = s.find(',', i, ht)
        while nextComma != -1:
            strLength = int(s[i:nextComma])
            strs.append(s[j:j+strLength])
            j += strLength
            i = nextComma + 1
            nextComma = s.find(',', i, ht)
        return strs