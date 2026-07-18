# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur=[]
        while True:
            if head in cur:
                return True

            if not head:
                return False
            cur.append(head)
            head=head.next
        