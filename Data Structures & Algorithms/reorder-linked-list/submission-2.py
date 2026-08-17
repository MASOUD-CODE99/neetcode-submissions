# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev=head
        cur=head.next
        while head:
            if cur:
                while cur.next:
                    cur=cur.next
                    prev=prev.next
            else:
                return
            ###################
            prev.next=None
            h=head
            hh=head.next
            cur.next=hh
            h.next=cur
            ####################
            head=head.next.next
            if head and head.next:
                cur=head.next
                prev=head
            else:
                return

            
        