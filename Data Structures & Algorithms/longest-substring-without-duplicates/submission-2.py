class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        max_length = 0
        seen = set()

        for r, char in enumerate(s):
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            max_length = max(max_length, len(seen))
        return max_length


        