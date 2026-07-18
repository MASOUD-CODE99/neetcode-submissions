class Solution:
    def __init__(self):
        self.ans=0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxe):
            if not node:
                return
            if node.val>=maxe:
                maxe=node.val
                self.ans+=1
                
            dfs(node.left,maxe)
            dfs(node.right,maxe)

        dfs(root, root.val)
        return self.ans
