class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                if stack:
                    x=int(stack.pop())
                if stack:
                    y=int(stack.pop())


                if tokens[i]=='+':
                    z=y+x
                    stack.append(z)


                elif tokens[i]=='-':
                    z=y-x
                    stack.append(z)
                    


                elif tokens[i]=='*':
                    z=y*x
                    stack.append(z)
                

                else :
                    z=int(y/x)
                    stack.append(z)




            else:
                stack.append(int(tokens[i]))

        return stack[-1]
