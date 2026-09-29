class Solution:
    def trap(self, height: List[int]) -> int:

        left = [0]
        maxLeft = 0
        right = [0]
        maxRight = 0
        water = []
        for i in range(1,len(height)):
            maxLeft = max(maxLeft, height[i-1])
            left.append(maxLeft)
        
        for i in range(len(height)-2, -1, -1): 
            maxRight = max(height[i+1], maxRight)
            right.append(maxRight)
            
        right.reverse()
        for i in range(len(height)):
            water.append(max(0, min(left[i], right[i]) - height[i]))
        
        return sum(water)


            




        