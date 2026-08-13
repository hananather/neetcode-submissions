class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0 
        L = 0
        ans = 0 
        for i in range(k):
            sum += arr[i]
        if sum/k >= threshold:
            ans+=1 
        
        for R in range(k, len(arr)):
            sum += arr[R]
            sum -= arr[L]
            L +=1
            if sum/k >= threshold:
                ans += 1
        return ans

        