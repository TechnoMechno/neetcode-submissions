# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        if not list1:
            return list2
        elif not list2:
            return list1
        
        
        if (list1.val <= list2.val):
            c1 = list1
            c2 = list2
        else:
            c1 = list2
            c2 = list1
        n1 = c1.next
        head = c1
    
        while n1 and c2:
            if c2.val < n1.val:
                c1.next = c2
                c1 = c2
                c2 = c2.next
            else:
                c1.next = n1
                c1 = n1
                n1 = n1.next
        
        if (not n1) and c2:
            c1.next = c2
        elif (not c2) and n1:
            c1.next = n1
        
        return head


        