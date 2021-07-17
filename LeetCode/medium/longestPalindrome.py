class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s):
            i=0
            j=len(s)-1
            #prin=j and (j-i >= 1):
                #printt(i,j)
            while i!=j and (j-i >= 1):
                if s[i] != s[j]:
                    return False
                else:
                    i=i+1
                    j=j-1
            return True
        size = len(s)
        dp=[]
        l=0
        longpalindrome=""
        for i in range(len(s)):
            for j in range((len(s)-1),-1,-1):
                if s[i] == s[j]:
                    substring=s[i:j+1]
                    #print(substring)
                    if len(substring)>l and (substring == substring[::-1]):
                        longpalindrome=substring
                        l=len(substring)
                    #break
        return longpalindrome
