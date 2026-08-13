class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check the rows
        valid = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        for row in board: 
            seen = set() 

            for curr in row:
                # skip '.' empty cells
                if curr == '.':
                    continue
                if curr not in valid:
                    return False
                if curr in seen:
                    return  False
                seen.add(curr)

        # now need to handle the columns
        for i in range(0,9):
            seen = set()
            for j in range(0,9):
                curr = board[j][i]
                if curr == '.':
                    continue
                if curr not in valid:
                    return False
                if curr in seen:
                    return  False
                seen.add(curr)
        # 3x3 checker
        for i in range(0,3):
            for j in range(0,3):
                seen = set()
                for h in range(i*3,i*3 +3):
                    for k in range(j*3, j*3 +3):
                            curr = board[h][k]
                            # skip '.' empty cells
                            if curr == '.':
                                continue
                            if curr not in valid:
                                return False
                            if curr in seen:
                                return  False
                            seen.add(curr)

        return True
            