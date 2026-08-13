class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(curr, start):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            d = digits[start]
            for i in range(len(digitToChar[d])):
                c = digitToChar[d][i]
                curr.append(c)
                backtrack(curr, start + 1)
                curr.pop()
        backtrack([], 0)
        return res


        