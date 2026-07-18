class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''
        for index, ch in enumerate(s):
            if ((ord('a') <= ord(ch) <= ord('z')) or
                ( ord('A') <= ord(ch) <= ord('Z'))or
                ( ord('0') <= ord(ch) <= ord('9'))):
                ss += ch.lower()

            
        if len(ss)%2 == 0:
            for i in range (int(len(ss)/2)):
                if not ss[i]==ss[-1*(i+1)]:
                    return False
        else :
            for i in range (int(len(ss)/2) +1):
                if not ss[i]==ss[-1*(i+1)]:
                    return False

        return True


            


        