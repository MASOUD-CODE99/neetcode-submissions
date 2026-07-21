class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""

        for c in s:
            if c.isalnum():     
                ss += c.lower() 
        l,r=0,len(ss)-1
        while r>l:
            if ss[r] != ss[l]:
                return False
            r-=1
            l+=1
        return True