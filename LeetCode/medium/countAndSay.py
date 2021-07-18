class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        num = "11"
        #res = []
        for i in range(2,n):
            print("i : ", i)
            count = 1
            temp = ""
            for j in range(1,len(num)):
                if num[j] == num[j-1]:
                    count = count + 1
                else:
                    #print(count,num[j-1])
                    temp = temp + str(count) + str(num[j-1])
                    count = 1
            num=temp+str(count) + str(num[j])
        return num
                
