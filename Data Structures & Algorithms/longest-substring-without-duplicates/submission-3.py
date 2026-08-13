class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the length
        max_length = 0
        l = 0
        window = set()
        for r in range(len(s)):
            # 1. check if the window is valid
            if s[r] in window:
                # make window vaild
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
            # window is valid
            window.add(s[r])
            max_length = max(max_length, (r -l) +1)
        return max_length
        