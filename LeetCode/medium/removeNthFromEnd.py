# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        temp = head
        while(temp):
            temp = temp.next
            count += 1
        index=count-n
        #print(count,index)
        if count == 1 and n == 1:
            return None
        if index == 0:
            curr = head.next
        else:
            curr = head
        count=1

        temp=ListNode()
        temp.next=curr
        while(curr):
            if count == index:
                if curr.next:
                    curr.next=curr.next.next
                    curr=curr.next
                else:
                    return None
            else:
                curr=curr.next
            count+=1
        #print(temp.next)
        return temp.next
