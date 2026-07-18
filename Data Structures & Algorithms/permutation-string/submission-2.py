class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1= [0] * 26
        freq2= [0] * 26
        n1=len(s1)
        n2=len(s2)
        l=0
        if n1>n2:
            return False
        i=0
        while(i<n1):
            freq1[ ord(s1[i]) - ord('a') ] += 1
            freq2[ ord(s2[i]) - ord('a') ] += 1
            i+=1

        for r in range(n1,n2):
            if freq1==freq2:
                return True
            else:
                freq2[ ord(s2[l]) - ord('a') ] -= 1
                freq2[ ord(s2[r]) - ord('a') ] += 1
                l+=1
        if freq1==freq2:
                return True
        return False


        

        