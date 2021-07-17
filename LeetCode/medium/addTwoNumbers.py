# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
            
def sortedList(llist):
        curr=llist
        slist,temp=[],[]
        while(curr):
            slist.append(curr.val)
            curr=curr.next
        for i in range(len(slist)-1,-1,-1):
            temp.append(slist[i])
        rev = "".join([str(i) for i in temp])
        return int(rev)
def add(temp):
    mylist=None
    for x in temp:
        print(x)
        mylist=ListNode(x,mylist)
        '''
        if mylist is None:
            mylist=y
        else:
            mylist=ListNode(y,mylist)
        '''
    return mylist
            
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=sortedList(l1)
        num2=sortedList(l2)
        #print(num1,num2)
        res=str(num1+num2)
        res = list(res)
        return add(res)
