class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n > 0):
            mod =  n%3    
            n = n//3
            #print(n,mod)
            if mod == 2:
                return False
        return True
            
