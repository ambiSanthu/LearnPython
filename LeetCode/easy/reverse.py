class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x = -x
            negative = True
        
        rev = 0
        while (x > 0):
            rem = x % 10
            rev = (rev * 10) + rem
            x = x // 10
            #print(x,rem,rev)
        if negative:
            rev=int(-rev)
        if -(2**31) > rev or 2**31 < rev:
            rev = 0  
        return rev
