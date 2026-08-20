# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=prev=ListNode()
        s1=""
        s2=""
        while l1 or l2:
            if l1:
                s1+=str(l1.val)
                l1=l1.next
            if l2:
                s2+=str(l2.val)
                l2=l2.next          
        s1= s1[::-1]
        s2= s2[::-1]
        x=int(s1)+int(s2)
        s=str(x)
        s=s[::-1]
        for x in s:
            node=ListNode(int(x))
            prev.next=node
            prev=node
        return dummy.next



