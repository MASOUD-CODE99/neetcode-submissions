class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1={}
        dic2={}
        ans=""
        l=0
        have=0
        need=0
        #######################
        for ch in t:
            dic1[ch] =dic1.get(ch, 0) + 1
            dic2[ch]=0
        need=len(dic1)
        #######################
        for r in range(len(s)):
            ###################
            if s[r] in dic1 :
                dic2[s[r]]+=1
                if dic1[s[r]] == dic2[s[r]]:
                    have+=1
            ###################
            if have==need:
                ##########
                substring = s[l:r+1]
                if len(substring)<len(ans) or not ans:
                    ans= substring
                ##########
                while  have==need and len(s)>l:
                    if s[l] in dic1:
                        dic2[s[l]] -= 1
                        if dic2[s[l]] < dic1[s[l]]:
                            have -= 1
                    substring = s[l:r+1]
                    if len(substring)<len(ans) or not ans:
                        ans= substring
                    l+=1
                ##########
        return ans


