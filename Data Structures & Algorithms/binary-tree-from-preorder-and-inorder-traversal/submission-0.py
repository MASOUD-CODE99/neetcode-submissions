class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return None

        # 1) root من preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2) مكانه في inorder
        mid = inorder.index(root_val)

        # 3) نبني ال left و right
        root.left = self.buildTree(
            preorder[1:],
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[mid+1:],
            inorder[mid+1:]
        )

        return root
