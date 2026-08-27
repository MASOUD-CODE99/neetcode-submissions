# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        d=True
        def dfs(root):
            nonlocal d
            if not root:
                return 0
            h_l=dfs(root.left)
            h_r=dfs(root.right)
            if abs(h_l-h_r)>1:
                d=False
            return max(h_l, h_r) + 1
        dfs(root)
        return d