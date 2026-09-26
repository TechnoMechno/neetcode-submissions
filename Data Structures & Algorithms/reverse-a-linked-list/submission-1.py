# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        current = head.next

        if current is None:
            return head
        prev.next = None
        while True:
            tmp = current.next
            if tmp is None:
                head = current
                current.next = prev
                break
            current.next = prev
            prev = current
            current = tmp
        
        return head
            