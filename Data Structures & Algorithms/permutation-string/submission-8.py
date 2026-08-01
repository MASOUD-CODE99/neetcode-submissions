class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        dic2={}
        for ch in s1:
            dic1[ch] =dic1.get(ch, 0) + 1
            dic2[ch]=0
        l=0
        for r in range(len(s2)): 
            if s2[r] in dic2:
                dic2[s2[r]]+=1
            if r - l + 1 > len(s1):
                if s2[l] in dic2:
                    dic2[s2[l]]-=1
                l += 1

            if dic1==dic2:
                return True
        return False