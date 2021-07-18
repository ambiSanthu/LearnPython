class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        total=0
        for i in range(n):
            arr.append((2*i)+1)
            total=total+((2*i)+1)
        num=int(total/n)
        ##print(num)
        count = 0
        for i in range(n,n//2,-1):
            temp=arr[i-1]-num
            count=count+temp
            #print(temp,count)
        return count
