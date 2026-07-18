class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])

        def dfs(r,c,visit,count):

            if count ==len(word):
                return True
            if (min(r,c)<0 or r==ROW or c==COL or((r,c) in visit) or board[r][c] != word[count]):
                return False

            visit.add((r,c))


            b1=dfs(r+1,c,visit,count+1)
            b2=dfs(r-1,c,visit,count+1)
            b3=dfs(r,c+1,visit,count+1)
            b4=dfs(r,c-1,visit,count+1)

            visit.remove((r,c))
            count-=1
            return b1 or b2 or b3 or b4



        def it (r,c):
            for r in range(ROW):
                for c in range(COL):
                    if dfs(r,c,set(),0):
                        return True
            return False



        if it(0,0):
            return True
        else:
            return False

