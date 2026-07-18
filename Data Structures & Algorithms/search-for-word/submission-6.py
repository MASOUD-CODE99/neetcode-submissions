class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])

        def dfs(r,c,visit,s):
            if (min(r,c)<0 or r==ROW or c==COL or( (r,c) in visit)):
                return False

            visit.add((r,c))
            s+=board[r][c]

            reversed_word = word[::-1]
            if word in s :
                return True

            b1=dfs(r+1,c,visit,s)
            b2=dfs(r-1,c,visit,s)
            b3=dfs(r,c+1,visit,s)
            b4=dfs(r,c-1,visit,s)

            visit.remove((r,c))
            return b1 or b2 or b3 or b4



        def it (r,c):
            for r in range(ROW):
                for c in range(COL):
                    if dfs(r,c,set(),""):
                        return True
            return False



        if it(0,0):
            return True
        else:
            return False

