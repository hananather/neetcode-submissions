class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
                return ""
        prefix = strs[0]
        for word in strs[1:]:
            i  = 0
            while i < min(len(prefix), len(word)):
                if word[i] != prefix[i]:
                    break
                i += 1
            prefix = prefix[:i]
        if len(prefix) > 0:
            return prefix
        return ""
                
