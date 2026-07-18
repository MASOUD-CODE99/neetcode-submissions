# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        lev=[]

        lis=[]

        if root:
            queue.append(root)
            lev.append(root.val)

        while len(queue) > 0:
            lis.append(lev)
            lev=[]
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    x=curr.left
                    lev.append(x.val)
                if curr.right:
                    queue.append(curr.right)
                    x=curr.right
                    lev.append(x.val)
        return lis