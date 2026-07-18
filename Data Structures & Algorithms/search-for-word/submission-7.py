class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])

        def dfs(r,c,visit,s,count):
            if (min(r,c)<0 or r==ROW or c==COL or( (r,c) in visit) or len(word)==count):
                return False

            visit.add((r,c))
            s+=board[r][c]

            if word in s :
                return True

            b1=dfs(r+1,c,visit,s,count+1)
            b2=dfs(r-1,c,visit,s,count+1)
            b3=dfs(r,c+1,visit,s,count+1)
            b4=dfs(r,c-1,visit,s,count+1)

            visit.remove((r,c))
            count-=1
            return b1 or b2 or b3 or b4



        def it (r,c):
            for r in range(ROW):
                for c in range(COL):
                    if dfs(r,c,set(),"",0):
                        return True
            return False



        if it(0,0):
            return True
        else:
            return False

