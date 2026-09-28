class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            # since the word start after # and j is at index
            start = j + 1
            res.append(s[start: start + l])
            i = start + l
        return res
        


