class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = 0
        y = x
        while y > 0:
            temp = temp * 10 + y%10
            y=y//10          
            #print(temp,y)
        if x == temp:
            return True
        else:
            return False
        
