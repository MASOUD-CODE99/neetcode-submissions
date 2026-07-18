# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=''
        s2=''
        while l1 is not None:
            s1+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            s2+=str(l2.val)
            l2=l2.next
        s1=s1[::-1]
        s2=s2[::-1]
        summ=int(s1)+int(s2)
        summ=str(summ)
        summ=summ[::-1]
        
        new_ll = ListNode(int(summ[0]))
        head=new_ll
        for i in range(1,len(summ)):
            new_node=ListNode(int(summ[i]))
            new_ll.next=new_node
            new_ll=new_ll.next
        return head





        