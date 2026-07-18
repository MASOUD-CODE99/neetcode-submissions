class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        bre,wind={},{}
        for c in t:
            bre[c]=1+bre.get(c,0)
        l=0
        have,need=0,len(t)
        long,ans=float("inf"),[0,0]

        for r in range(len(s)):
            c=s[r]
            wind[c]=1+wind.get(c,0)
            if c in bre and wind[c]==bre[c]:
                have+=bre[c]
            while have==need:
                if s[l] in bre and wind[s[l]]==bre[s[l]]:
                    if long>r-l+1:
                        long=r-l+1
                        ans=[l,r]
                    wind[s[l]]-=1
                    l+=1
                    have-=bre[c]
                else:
                    wind[s[l]]-=1
                    l+=1
        return "" if long == float("inf") else s[ans[0]:ans[1]+1]
            

        