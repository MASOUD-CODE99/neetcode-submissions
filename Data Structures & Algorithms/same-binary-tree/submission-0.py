# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        fi,se=q,p
        st1,st2=[],[]
        def recfi(fi):
            if not fi :
                st1.append(None)
                return 
            recfi(fi.left)
            recfi(fi.right)
            st1.append(fi.val)
        def recse(se):
            if not se :
                st2.append(None)
                return 
            recse(se.left)
            recse(se.right)
            st2.append(se.val)
        recfi(fi)
        recse(se)
        if len(st1)!=len(st2):
            return False
        else:
            while st1:
                if st1[-1] != st2[-1]:
                    return False
                st1.pop()
                st2.pop()
        return True
            
        