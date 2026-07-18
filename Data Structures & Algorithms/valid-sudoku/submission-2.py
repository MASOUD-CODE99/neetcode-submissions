class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            dect={}
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in dect:
                        return False  
                    dect[num] = True
        


        for i in range(9):
            dect={}
            for j in range(9):
                num = board[j][i]
                if num != '.':
                    if num in dect:
                        return False  
                    dect[num] = True
        ii=0
        for i in range(3):
            jj=0
            for j in range(3):

                dect={}
                for x in range (ii,ii+3):
                    for y in range(jj,jj+3):
                        num = board[x][y]
                        if num != '.':
                            if num in dect:
                                return False  
                            dect[num] = True 
                                           

                jj+=3
            ii+=3
        return True

















