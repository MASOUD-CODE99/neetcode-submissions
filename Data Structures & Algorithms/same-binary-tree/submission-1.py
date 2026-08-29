# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        d=True
        def dfs(p,q):
            nonlocal d
            if not p and not q:
                return
            elif (not p and q) or (not q and p) or  (q.val != p.val) :
                d=False
                return
            dfs(p.left,q.left)
            dfs(p.right,q.right)
        dfs(p,q)
        return d