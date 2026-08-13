class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0 # left pointer
        freq = {}
        for r in range(len(s)):
            # compute the most frequent element in window
            freq[s[r]] = freq.get(s[r], 0) + 1
            # check if valid window
            # window_length = r - l +1
            while ((( r - l +1) - max(freq.values())) > k):
                freq[s[l]] -= 1
                l += 1
            max_length = max(( r - l +1), max_length)
        return max_length

