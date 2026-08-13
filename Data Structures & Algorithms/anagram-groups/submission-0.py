class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        dic = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in dic:
                dic[s].append(i) 
            else: 
                dic[s] = [i]
        return list(dic.values())
    

        