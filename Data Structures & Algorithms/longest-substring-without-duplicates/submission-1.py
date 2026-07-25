class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=set()
        maxnum=0
        l=0
        for r in range(len(s)):
            if s[r] in ss:
                while s[r] != s[l]:
                    ss.remove(s[l])
                    l+=1
                ss.remove(s[l])
                l+=1
            ss.add(s[r])
            maxnum=max(r-l+1,maxnum)
        return maxnum