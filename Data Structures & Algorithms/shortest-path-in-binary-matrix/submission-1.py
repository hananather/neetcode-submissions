class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        def is_valid(r, c):
            return 0 <= r < n and 0 <= c < m and grid[r][c] == 0

        n, m = len(grid), len(grid[0])

        seen = set()
        queue = deque()
        queue.append((0,0,1))
        seen.add((0,0))

        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1, -1), (-1,-1)]

        while queue:
            r, c, step = queue.popleft()
            if (r, c) == (n-1, m-1):
                return step

            for dr, dc in directions:
                n_row, n_col = r + dr, c + dc
                if is_valid(n_row, n_col) and (n_row, n_col) not in seen:
                    queue.append((n_row, n_col, step + 1))
                    seen.add((n_row, n_col))
        return -1
                
        