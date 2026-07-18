class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        ans=[]

        def helper(op,end):
            if op==end==n:
                s = "".join(stack)
                ans.append(s)
                return
            
            if n>op:
                stack.append("(")
                helper(op+1,end)
                stack.pop()
            
            if n>end and op>end:
                stack.append(")")
                helper(op,end+1)
                stack.pop()


        helper(0,0)
        return ans