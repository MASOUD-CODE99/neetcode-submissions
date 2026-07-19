class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for n in tokens:
            if n =="+":
                x2=int(st[-1])
                x1=int(st[-2])
                st.pop()
                st.pop()
                st.append(x1+x2)
            elif n=="-":
                x2=int(st[-1])
                x1=int(st[-2])
                st.pop()
                st.pop()
                st.append(x1-x2)
            elif n=="*":
                x2=int(st[-1])
                x1=int(st[-2])
                st.pop()
                st.pop()
                st.append(x1*x2)
            elif n=="/":
                x2=int(st[-1])
                x1=int(st[-2])
                st.pop()
                st.pop()
                st.append(x1/x2)
            else:
                st.append(n)
        return int(st[-1])
                















        