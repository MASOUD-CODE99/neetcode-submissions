class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        lis=[]
        for s in strs:
            x = "".join(sorted(s))
            dic[x].append(s)
        return list(dic.values())