class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[" :
                st.append(ch)
            elif (st) and ((ch==")" and st[-1]=="(") or (ch=="]" and st[-1]=="[") or (ch=="}" and st[-1]=="{")): 
                st.pop()
            else:
                st.append(ch)
        if not st:
            return True
        else:
            return False