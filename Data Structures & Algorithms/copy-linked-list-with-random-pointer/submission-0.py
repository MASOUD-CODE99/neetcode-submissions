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
        mp={}
        if head is None:
            return None
        orig = head
        new_head = Node(orig.val) 
        copy_ptr = new_head
        mp[orig]=copy_ptr

        while orig.next is not None:
            orig = orig.next
            copy_ptr.next = Node(orig.val)
            copy_ptr = copy_ptr.next
            mp[orig]=copy_ptr
        cpy=head
        ll=new_head
        while cpy is not None:
            po1=cpy
            po2=cpy.random
            pn1=mp[cpy]
            pn2 = mp.get(po2)
            ll.random=pn2
            cpy=cpy.next
            ll=ll.next
        return new_head





