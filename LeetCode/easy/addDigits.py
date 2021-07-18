class Solution:
    def addDigits(self, num: int) -> int:
        #print(num,num//10)
        if num // 10 == 0:
            return num
        else:
            add = 0
            while num:
                add = add + num % 10
                num = num//10
            #print(add)
            return self.addDigits(add)
