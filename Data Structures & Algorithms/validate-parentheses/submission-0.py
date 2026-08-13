class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
        '(': ')',
        '{': '}',
        '[': ']'
        }
        stack = []
        for char in s:
            if char in valid:
                stack.append(char)
            if char in valid.values():
                if not stack:
                    return False
                if valid[stack.pop()] != char:
                    return False
        return len(stack) == 0



        