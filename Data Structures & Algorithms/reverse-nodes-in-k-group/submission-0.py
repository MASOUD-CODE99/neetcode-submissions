# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        node=fast=dummy=ListNode()
        node.next=head
        slow=head
        flag=False

        while True:
            kk=k
            fast=slow
            while fast and kk:
                fast=fast.next
                kk-=1

            if kk==0:
                kkk=k
                prev=None
                cur=slow
                while kkk:
                    x=cur
                    cur=cur.next
                    x.next=prev
                    prev=x
                    kkk-=1
                node.next=x
                node=slow
                slow.next=cur
                slow=slow.next

            else:
                return dummy.next



        