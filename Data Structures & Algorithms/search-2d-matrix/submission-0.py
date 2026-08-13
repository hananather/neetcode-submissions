class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        low, high = 0 , m*n-1
        while low <= high: # think about this condition
            mid = (low + high) //2 
            row = mid // n
            col = mid % n 
            val = matrix[row][col]

            if target == val:
                return True
            if target < val:
                high = mid -1
            else:
                low = mid + 1
        return False


