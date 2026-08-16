# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h=head
        hh=head

        while h and hh:
            if h and hh.next:
                h=h.next
                hh=hh.next.next
            else:
                return False
            if h==hh:
                return True

        return False

        