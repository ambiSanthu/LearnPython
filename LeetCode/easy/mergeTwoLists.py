# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output=ListNode()
        head=output
        while l1 or l2:
            #print(l1.val,l2.val)
            if not l1:
                output.next = l2
                l2=l2.next
            elif not l2:
                output.next = l1
                l1=l1.next
            elif l1.val < l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            #if output.next:
            output=output.next
               
        return head.next
