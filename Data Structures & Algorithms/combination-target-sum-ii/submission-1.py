class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(path, curr, start):
            if curr == target and path not in res:
                res.append(path[:])
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate + curr <= target: 
                    path.append(candidate)
                    backtrack(path, curr + candidate, i+1 ) # its +1 since we don't want dups
                    path.pop()
        backtrack([], 0, 0)
        return res


        