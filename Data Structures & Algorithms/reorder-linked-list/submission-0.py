# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        st=[]
        while fast and fast.next:
            st.append(slow)
            slow = slow.next
            fast = fast.next.next
        if fast:
            x=slow
            slow=slow.next           
            x.next=None
            while st and slow:
                node=st.pop()
                temp=slow.next
                node.next=slow
                slow.next=x
                x=node
                slow=temp
        else:
            x=None
            while st and slow:
                node=st.pop()
                temp=slow.next
                node.next=slow
                slow.next=x
                x=node
                slow=temp
                
            