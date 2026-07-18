class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=1
        long=1
        if len(s)==0:
            return 0;
        n=len(s)
        freq={}
        freq[s[0]]=1
        while(n>r):
            if s[r] not in freq or freq[s[r]]==0:
                freq[s[r]]=1
                long=max(long,r-l+1)
                r+=1
            else:
                while True:
                    if s[l]==s[r]:
                        r+=1
                        l+=1
                        break
                    else:
                        freq[s[l]]-=1
                        l+=1
                long=max(long,r-l)
        return long
                


        