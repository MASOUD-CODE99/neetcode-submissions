class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            return (
                check(root.left, subRoot.left)
                and check(root.right, subRoot.right)
            )

        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if check(root, subRoot):
                    return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root)