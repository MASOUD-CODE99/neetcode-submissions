# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.lis=[]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def ans(root):
            if not root :
                return
            ans(root.left)
            self.lis.append(root.val)
            ans(root.right)
        ans(root)
        return self.lis[k-1]

                
                
        
