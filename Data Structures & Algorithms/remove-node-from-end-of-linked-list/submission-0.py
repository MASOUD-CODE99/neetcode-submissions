# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            nxt = cur.next    
            cur.next = prev   
            prev = cur      
            cur = nxt        
        n-=1
        h=prev
        if n==0:
            h=prev.next
        else:
            while prev:
                if  n==1:
                    prev.next=prev.next.next
                    prev=prev.next
                else:
                    prev=prev.next
                n-=1 
        prev=None
        cur=h
        while cur:
            nxt = cur.next    
            cur.next = prev   
            prev = cur      
            cur = nxt  
        return prev
         
