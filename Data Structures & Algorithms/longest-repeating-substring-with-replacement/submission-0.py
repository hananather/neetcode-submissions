class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force
        max_length = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                most_freq = max(freq.values())
                if len(s[i:j+1]) - most_freq <= k:
                    max_length = max(len(s[i:j+1]), max_length)
        return max_length







        