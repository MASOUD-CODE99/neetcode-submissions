# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=node=ListNode()
        node.next=head
        cur=head
        ##################
        s=0
        while cur:
            s+=1
            cur=cur.next
        ####################
        ss=s-n+2
        cur=node
        prev=None
        while True:
            ss-=1
            if ss==0:
                prev.next=cur.next
                break
            prev=cur
            cur=cur.next

        return node.next
            
        