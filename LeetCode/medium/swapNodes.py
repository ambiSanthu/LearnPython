# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        count = 0
        temp = head
        swapNode = toswapNode = 0
        while(temp):
            count += 1
            if count == k:
                swapval = temp.val
            temp=temp.next
            
        lastk = count - k + 1
       # print(count,k,lastk)
        
        count = 0
        temp = head
        while(temp):
            count += 1
            if count == lastk:
                toswapval = temp.val
                break
            temp=temp.next   
       # print(swapNode,toswapNode)  
        
        temp=ListNode()
        temp.next = head
            
        count = 0
        while(head):
            count+=1
            if count == k:
                head.val=toswapval
                head=head.next
            elif count == lastk:
                head.val=swapval
                head = head.next
            else:
                head = head.next
        return temp.next
        
        
