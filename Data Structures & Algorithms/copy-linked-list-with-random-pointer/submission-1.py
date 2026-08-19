"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=node=prev=Node(0)
        dic={}
        cur=head
        while cur:
            n=Node(cur.val)
            prev.next=n
            prev=n
            dic[cur]=n
            ###############
            cur=cur.next
        ####################
        cur=head
        copy=node.next
        while cur:
            copy.random=dic.get(cur.random)
            copy=copy.next
            cur=cur.next
        return node.next