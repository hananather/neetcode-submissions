class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        fresh = 0 
        n = len(grid)
        m = len(grid[0])
        
        queue = deque()
        seen = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j,0))
                    seen.add((i, j))

        if fresh == 0:
            return 0
        # fresh: yes, rotten fruit: no
        if not seen:
            return -1

        directions = [(0,1), (0, -1), (1,0), (-1,0)]

        def is_valid(r,c):
            return 0 <= r < n and 0 <= c < m

        while queue:
            r, c, step = queue.popleft()
    
            
            for dr, dc in directions:
                n_row, n_col = r + dr, c + dc
                if is_valid(n_row, n_col) and (n_row, n_col) not in seen:
                    if grid[n_row][n_col] == 1:
                        fresh -= 1
                        queue.append((n_row, n_col, step + 1))
                    seen.add((n_row, n_col))
        return step if fresh == 0 else -1