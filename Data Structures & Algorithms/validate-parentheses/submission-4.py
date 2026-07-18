class Solution:
    def isValid(self, s: str) -> bool:
        x=0
        stack=[]
        for ch in s:
            if ch =='{' or ch=='[' or ch =='(':
                stack.append(ch)
                x+=1
            elif stack and ((ch =="]"and stack[-1] =='[') or (ch =="}"and stack[-1] =='{') or( ch ==")"and stack[-1] =='(')):
                stack.pop()
                x-=1
            else :
                return False
        if x==0:
            return True
        else:
            return False
                    
