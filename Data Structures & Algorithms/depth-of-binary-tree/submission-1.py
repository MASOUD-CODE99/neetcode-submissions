# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxe = 0
        self.k = 0
        self.flag=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root and self.flag==0:
            return 0
        else:
             self.flag=1
        

        if not root:
            return
        self.k+=1

        if not root.left and not root.right:
            self.maxe=max(self.maxe,self.k)
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.k-=1


        return self.maxe

        
        