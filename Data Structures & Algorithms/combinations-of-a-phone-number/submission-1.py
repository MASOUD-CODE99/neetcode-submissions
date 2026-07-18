class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []







        main_str=["abc", "def", "ghi", "jkl", "mno","pqrs", "tuv","wxyz"]
        s=[]
        for x in digits:
            s.append(main_str[int(x)-2])
        ans=[]
        cur=""
        n=len(s)




        def bt(s,n,ans,cur,x,y):
            if len(cur)==n:
                ans.append(cur)
                return

            for  yy in range(len(s[x])):
                cur+=s[x][yy]
                bt(s,n,ans,cur,x+1,y)
                cur = cur[:-1] 





        bt(s,n,ans,cur,0,0)
        return ans
