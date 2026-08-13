class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for idx, char in enumerate(s):
            seen = set()
            for j in s[idx:]: # loop over the remaining list
                if j in seen:
                    break
                else:
                    seen.add(j)
                max_length = max (max_length, len(seen))
        return max_length     