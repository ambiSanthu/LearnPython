# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        counter=0
        pointer = head
        while (pointer and (pointer.next != None)):
            pointer = pointer.next
            counter=counter+1
        #print(counter)
        if counter == 0 :
            return head
        else:
            k=k%(counter+1)
        for i in range(k):
            pointer = head
            previous = head
            while (pointer and (pointer.next != None)):
                previous = pointer
                pointer = pointer.next   
            if previous and previous.next != None:
                previous.next=None
                pointer.next=head
                head=pointer
        return head
