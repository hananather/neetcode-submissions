class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def is_valid(r,c):
            return  (0 <= r < n) and (0 <= c < m) and (grid[r][c] == 1)
        
        def dfs(r,c, counts):

            for dr, dc in directions:
                n_row, n_col = r + dr, c + dc
                if (n_row, n_col) not in seen and is_valid(n_row, n_col):
                    counts += 1
                    seen.add((n_row, n_col))
                    counts = dfs(n_row, n_col, counts)
            return counts
                    


        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set()
        ans = 0 
        for i in range(n):
            for j in range(m):
                if is_valid(i,j) and (i,j) not in seen:
                    seen.add((i,j))
                    ans = max(dfs(i,j, 1), ans)
        return ans