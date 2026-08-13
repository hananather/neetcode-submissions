class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def is_valid(r,c):
            if 0<= r < m and 0<= c < n:
                return True
            return False
        
        steps = [(0,1),(0,-1), (1,0), (-1,0)]
        seen = set()
        def backtrack(i, r, c):
            if i == len(word):
                return True
            seen.add((r,c))
            for dr, dc in steps:
                new_r, new_c = dr + r, dc + c
                if is_valid(new_r, new_c) and (new_r, new_c) not in seen and board[new_r][new_c] == word[i]:
                    if backtrack(i+1, new_r, new_c):
                        return True
            seen.remove((r,c))


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(1, i, j):
                        return True
        return False

